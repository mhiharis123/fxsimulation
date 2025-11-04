# Quick Start - Dokploy Deployment

## 30-Second Setup

### Option 1: Using Dokploy Dashboard (Recommended)

1. **In Dokploy Dashboard:**
   - New Application → Docker
   - Connect GitHub repo
   - Select `main` branch
   - Dockerfile: `/Dockerfile`
   - Port: `5000`
   - Deploy!

### Option 2: Using Docker Locally First

```bash
# Test locally
docker-compose up

# Then push to Dokploy
```

## Key Files for Deployment

| File | Purpose |
|------|---------|
| `Dockerfile` | Docker image configuration |
| `docker-compose.yml` | Local testing |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Git exclusions |
| `DOKPLOY_SETUP.md` | Full deployment guide |

## What Gets Deployed

✅ Flask web application (app.py)
✅ HTML templates (AM & PM sheets)
✅ Excel data file
✅ All Python dependencies

## After Deployment

1. Access: `https://your-domain.com`
2. AM Sheet: Home page
3. PM Sheet: `/pm` path
4. Both sheets fully functional with:
   - Real-time calculations
   - Rate adjustments
   - Global markup override
   - Reset functionality

## Common Commands

```bash
# Test Docker locally
docker-compose build
docker-compose up

# View logs
docker-compose logs -f

# Stop container
docker-compose down
```

## Troubleshooting Checklist

- [ ] Git repo public and accessible
- [ ] All files committed and pushed
- [ ] `requirements.txt` has all dependencies
- [ ] `Dockerfile` paths are correct
- [ ] Port 5000 is available
- [ ] Domain DNS configured

## Support Files

- **DOKPLOY_SETUP.md** - Complete setup guide
- **README.md** - Application documentation
- **fx_profit_calc_logic.md** - Calculation logic

## Next Steps

1. Commit changes:
   ```bash
   git add Dockerfile docker-compose.yml requirements.txt .gitignore .env.example
   git commit -m "Add Docker and Dokploy deployment configuration"
   git push
   ```

2. Go to Dokploy dashboard and create new application

3. Point to your repository and deploy!

That's it! Your app will be live in minutes.
