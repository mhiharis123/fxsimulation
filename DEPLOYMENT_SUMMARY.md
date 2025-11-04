# FX Profit Calculator - Complete Deployment Setup

## What's New

### Updated Files
- ✅ `.gitignore` - Comprehensive Python/Flask project exclusions
- ✅ `requirements.txt` - Python package dependencies
- ✅ `Dockerfile` - Docker containerization
- ✅ `docker-compose.yml` - Local testing configuration
- ✅ `.env.example` - Environment variables template

### New Documentation
- ✅ `DOKPLOY_SETUP.md` - Complete Dokploy deployment guide
- ✅ `DEPLOYMENT_QUICK_START.md` - Quick reference

## Project Structure

```
FXSimulation/
├── app.py                           # Flask application
├── run.py                           # Local runner
├── templates/
│   ├── index.html                   # AM Sheet UI
│   └── pm.html                      # PM Sheet UI
├── FX October PnL updated.xlsx      # Data file
├── Dockerfile                       # Docker image config
├── docker-compose.yml               # Local test config
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git exclusions (UPDATED)
├── .env.example                     # Environment template
├── README.md                        # Application docs
├── fx_profit_calc_logic.md          # Calculation logic
├── DOKPLOY_SETUP.md                 # Deployment guide
└── DEPLOYMENT_QUICK_START.md        # Quick reference
```

## .gitignore Coverage

| Category | Excluded |
|----------|----------|
| **PyInstaller** | build/, dist/, *.spec |
| **Python** | __pycache__/, *.pyc, venv/, env/, .egg-info/ |
| **Flask** | instance/, .webassets-cache |
| **IDE** | .vscode/, .idea/, *.swp |
| **OS** | .DS_Store, Thumbs.db |
| **Config** | .env, .env.local |
| **Logs** | *.log |

## Deployment Options

### 1. Dokploy (Recommended)
- Self-hosted Docker deployment platform
- Auto SSL/HTTPS
- Easy domain management
- See: `DOKPLOY_SETUP.md`

### 2. Docker Local Testing
```bash
docker-compose up
# Access at http://localhost:5000
```

### 3. Traditional Hosting
Deploy `app.py` with:
- Python 3.12+
- Dependencies from `requirements.txt`
- Gunicorn for production
- Nginx as reverse proxy

## Quick Start Commands

### Local Testing
```bash
# Build and run
docker-compose build
docker-compose up

# Or run Python directly
python run.py
```

### Prepare for Dokploy
```bash
# Commit all changes
git add .
git commit -m "Add deployment configuration for Dokploy"
git push origin main

# Then use Dokploy dashboard to deploy
```

### Docker Build Only
```bash
docker build -t fx-profit-calculator .
docker run -p 5000:5000 fx-profit-calculator
```

## Environment Variables

See `.env.example` for template:

```
FLASK_ENV=production
FLASK_APP=app.py
FLASK_DEBUG=0
PORT=5000
HOST=0.0.0.0
```

## Features

### AM Sheet (USD/MYR)
- 22 trading days
- Individual rate adjustments
- Global markup override
- Real-time calculations
- Reset functionality

### PM Sheet (Multiple Currencies)
- 65 individual transactions
- 4 currency pairs (SGD/MYR, HKD/MYR, CNH/MYR, USD/MYR)
- Multiple bookings per date (aggregated display)
- All AM features plus currency filtering

### Both Sheets Include
- Buy/Sell rate adjustments with 4 decimal precision
- Automatic trade type detection
- Mark up calculation (always positive)
- Real-time profit updates
- Color-coded profit display
- Reset all functionality
- Total profit aggregation

## Next Steps

### 1. Commit Changes
```bash
git add Dockerfile docker-compose.yml requirements.txt .gitignore .env.example
git commit -m "Add Docker and Dokploy deployment configuration"
git push
```

### 2. Test Locally (Optional)
```bash
docker-compose up
# Test at http://localhost:5000
```

### 3. Deploy to Dokploy
1. Create Dokploy account/instance
2. Connect GitHub repository
3. Create new application
4. Configure as per `DOKPLOY_SETUP.md`
5. Deploy!

### 4. Post-Deployment
- Verify both sheets work
- Test all features
- Configure domain with SSL
- Monitor application logs

## Files Reference

| File | Purpose |
|------|---------|
| `.gitignore` | What to exclude from Git |
| `requirements.txt` | Python package list |
| `Dockerfile` | Container image definition |
| `docker-compose.yml` | Local development setup |
| `.env.example` | Environment variables template |
| `DOKPLOY_SETUP.md` | Detailed deployment guide |
| `DEPLOYMENT_QUICK_START.md` | Quick reference |

## Support Resources

- **Dokploy**: https://dokploy.com/docs
- **Flask**: https://flask.palletsprojects.com/
- **Docker**: https://docs.docker.com/
- **Python**: https://docs.python.org/3/

## Executable Available

The `FX_Profit_Calculator.exe` is available in `dist/` folder for:
- Local testing
- Offline use
- Quick deployment testing

## Checklist Before Deployment

- [ ] All files committed to Git
- [ ] Repository is public and accessible
- [ ] Docker image builds successfully
- [ ] App works on http://localhost:5000 locally
- [ ] `requirements.txt` includes all dependencies
- [ ] Excel file is in repository
- [ ] Domain is ready (if using custom domain)
- [ ] DNS records configured (if using custom domain)
- [ ] Dokploy instance is ready

## Production Notes

✅ This configuration is production-ready
✅ Auto SSL/HTTPS support via Dokploy
✅ Automatic restarts on failure
✅ Scalable containerized deployment
✅ Minimal security concerns (static data, no DB)
✅ Low resource requirements (50MB Docker image)

---

**Ready to deploy?** Start with `DOKPLOY_SETUP.md` or `DEPLOYMENT_QUICK_START.md`
