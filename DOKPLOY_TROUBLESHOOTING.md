# Dokploy Deployment - Troubleshooting Guide

## Common Errors & Solutions

### Error 1: "Build dockerfile failed"

**Cause**: Usually a file path issue in Dockerfile

**Solution**:
✅ Use quotes for filenames with spaces: `COPY "FX October PnL updated.xlsx" ./`
✅ Use forward slashes: `./templates/` not `.\templates\`
✅ Ensure all files exist in repository

### Error 2: "File not found: FX October PnL updated.xlsx"

**Cause**: Excel file not committed to Git

**Solution**:
```bash
# Add Excel file to Git
git add "FX October PnL updated.xlsx"
git commit -m "Add Excel data file"
git push
```

### Error 3: Port already in use

**Cause**: Port 5000 is occupied

**Solution**: In Dokploy, change port mapping or ensure no other app uses 5000

### Error 4: ModuleNotFoundError or ImportError

**Cause**: Missing dependencies in requirements.txt

**Solution**:
```bash
# Verify requirements.txt contains all needed packages
cat requirements.txt

# Should include:
# Flask==3.0.0
# openpyxl==3.11.2
# Werkzeug==3.0.1
# Jinja2==3.1.2
```

### Error 5: "Application failed to start"

**Cause**: Several possibilities

**Solution**:
1. Check Dokploy logs for specific error
2. Verify Excel file path in app.py:
   ```python
   calculator = FXProfitCalculator('FX October PnL updated.xlsx')
   ```
3. Test locally first:
   ```bash
   docker-compose up
   ```

### Error 6: "No such file or directory: app.py"

**Cause**: COPY command failed in Dockerfile

**Solution**:
- Ensure Dockerfile uses correct paths
- Verify file exists in repository
- Use quotes for special characters

---

## Pre-Deployment Checklist

### Git Repository
- [ ] All Python files committed
- [ ] Excel file committed (`git add "FX October PnL updated.xlsx"`)
- [ ] Dockerfile committed
- [ ] docker-compose.yml committed
- [ ] requirements.txt committed
- [ ] templates/ directory committed
- [ ] All changes pushed to main branch

### Files Exist
- [ ] app.py exists
- [ ] run.py exists
- [ ] templates/index.html exists
- [ ] templates/pm.html exists
- [ ] FX October PnL updated.xlsx exists
- [ ] requirements.txt exists
- [ ] Dockerfile exists

### Dockerfile Correctness
- [ ] Uses quotes for filenames with spaces: `"FX October PnL updated.xlsx"`
- [ ] Uses forward slashes: `./templates/` not `.\templates\`
- [ ] EXPOSE 5000 is set
- [ ] CMD ["python", "app.py"] is correct

### Dependencies
- [ ] requirements.txt has Flask==3.0.0
- [ ] requirements.txt has openpyxl==3.11.2
- [ ] requirements.txt has Werkzeug==3.0.1
- [ ] requirements.txt has Jinja2==3.1.2

---

## Local Testing Before Deployment

```bash
# 1. Build locally
docker-compose build

# 2. Run locally
docker-compose up

# 3. Test in browser
# http://localhost:5000  <- AM Sheet
# http://localhost:5000/pm <- PM Sheet

# 4. Check logs
docker-compose logs -f

# 5. Stop
docker-compose down
```

If local test works, Dokploy deployment should work too!

---

## Dokploy Configuration Verification

### Application Settings
1. **Name**: fx-profit-calculator
2. **Type**: Docker
3. **Repository**: Correctly connected GitHub
4. **Branch**: main
5. **Dockerfile Path**: Dockerfile (or /Dockerfile)

### Build Settings
- **Build Command**: Leave empty
- **Publish Directory**: Leave empty

### Port Settings
- **Port**: 5000
- **Protocol**: HTTP (HTTPS handled by reverse proxy)

### Environment Variables
```
FLASK_ENV=production
FLASK_APP=app.py
FLASK_DEBUG=0
```

---

## Enable Debug Logging in Dokploy

To see detailed build logs:

1. In Dokploy dashboard
2. Go to Application → Logs
3. Watch real-time build output
4. Copy any error messages for debugging

---

## Manual Deploy Steps

If automated deploy fails:

```bash
# 1. SSH into Dokploy server
ssh user@dokploy-server

# 2. Navigate to app directory
cd /path/to/app

# 3. Pull latest code
git pull origin main

# 4. Rebuild image
docker build -t fx-profit-calculator .

# 5. Stop old container
docker stop fx-profit-calculator || true

# 6. Run new container
docker run -d -p 5000:5000 \
  -e FLASK_ENV=production \
  -e FLASK_APP=app.py \
  --name fx-profit-calculator \
  fx-profit-calculator

# 7. Check logs
docker logs fx-profit-calculator
```

---

## Verify Deployment Success

### In Browser
1. Navigate to: `https://your-domain.com`
2. Should see AM Sheet
3. Try PM Sheet at `/pm`
4. Test functionality:
   - Adjust rates
   - Use global markup override
   - Check total profit updates

### Using curl
```bash
# Test AM Sheet
curl https://your-domain.com/

# Test PM Sheet
curl https://your-domain.com/pm

# Test API
curl https://your-domain.com/api/get-data
```

### Check Container Health
```bash
# SSH to server, then:
docker ps  # See running containers
docker logs fx-profit-calculator  # View logs
docker stats  # View resource usage
```

---

## Performance Issues

### App Slow to Start
- Normal: Excel file is loaded on startup (takes 2-5 seconds)
- First request may be slow
- Subsequent requests are instant

### High Memory Usage
- Normal: Flask app uses ~100-200MB
- Excel file cached in memory (~50MB)
- Calculations happen in-memory (fast)

### Port Issues
```bash
# Check if port 5000 is in use
lsof -i :5000

# Kill process if needed
kill -9 <PID>
```

---

## Common Success Indicators

✅ Deployment completes without errors
✅ App appears in Dokploy dashboard as "Running"
✅ Can access https://your-domain.com in browser
✅ Both AM and PM sheets load
✅ Rate adjustments work in real-time
✅ Global markup override functions
✅ Total profit updates correctly

---

## Still Not Working?

1. **Provide error messages** from Dokploy logs
2. **Check Git status**: `git status`
3. **Verify files exist**: `ls -la`
4. **Test locally first**: `docker-compose up`
5. **Review Dockerfile**: Ensure correct file paths
6. **Check requirements.txt**: All dependencies listed

---

## Quick Fix Checklist

If deployment keeps failing:

```bash
# 1. Add Excel file to Git
git add "FX October PnL updated.xlsx"

# 2. Verify Dockerfile
cat Dockerfile

# 3. Verify requirements.txt
cat requirements.txt

# 4. Commit and push
git commit -m "Fix deployment configuration"
git push origin main

# 5. Retry Dokploy deploy
# (Go to Dokploy dashboard and click Deploy)
```

---

## Getting Help

**Dokploy Support**: https://dokploy.com/docs
**Docker Support**: https://docs.docker.com/
**Flask Support**: https://flask.palletsprojects.com/

Include these when asking for help:
- Full error message from logs
- Output of `docker-compose up` locally
- Git log showing recent commits
- Dockerfile contents
