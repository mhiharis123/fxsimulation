# Dokploy Deployment Guide - FX Profit Calculator

## Overview
This guide explains how to deploy the FX Profit Calculator Flask application to Dokploy.

## Prerequisites
- Dokploy instance running (self-hosted)
- Git repository with this code pushed to GitHub/GitLab
- Docker and Docker Compose installed (for local testing)

## Setup Instructions

### 1. Local Testing with Docker

Test the Docker image locally before deploying to Dokploy:

```bash
# Build the Docker image
docker-compose build

# Run the container
docker-compose up

# Access the app at http://localhost:5000
```

### 2. Prepare Repository

Ensure your repository structure looks like this:

```
FXSimulation/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
├── run.py
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   └── pm.html
└── FX October PnL updated.xlsx
```

### 3. Push to Repository

```bash
git add .
git commit -m "Add Dokploy deployment configuration"
git push origin main
```

### 4. Dokploy Configuration

#### Step 1: Create New Project in Dokploy
1. Log in to Dokploy dashboard
2. Go to **Projects** → **Create New Project**
3. Enter project name: `FX-Profit-Calculator`
4. Select your hosting server

#### Step 2: Add Application
1. In your project, go to **Applications** → **Create New Application**
2. Configure as follows:

**Basic Settings:**
- Application Name: `fx-profit-calculator`
- Application Type: **Docker**

**Repository Settings:**
- Select your Git provider (GitHub, GitLab, etc.)
- Repository: `yourusername/FXSimulation` (or your repo name)
- Branch: `main` (or your default branch)
- Dockerfile Path: `Dockerfile`

**Build Settings:**
- Build Command: Leave empty (Docker handles it)
- Publish Directory: Leave empty

**Port Settings:**
- Port: `5000`
- Protocol: `HTTP`

#### Step 3: Environment Variables
In Dokploy, add these environment variables:

```
FLASK_ENV=production
FLASK_APP=app.py
```

#### Step 4: Domain Configuration
1. Go to **Settings** → **Domains**
2. Add your domain: `your-domain.com`
3. Enable SSL/HTTPS (Dokploy can auto-generate Let's Encrypt certificates)

#### Step 5: Deploy

1. Click **Deploy** button
2. Monitor deployment logs
3. Once complete, access your app at `https://your-domain.com`

## File Descriptions

### Dockerfile
- Specifies the Python 3.12 base image
- Installs dependencies from `requirements.txt`
- Copies application files
- Exposes port 5000
- Sets up Flask environment

### docker-compose.yml
- Local development configuration
- Maps port 5000
- Mounts the Excel file as volume
- Auto-restart policy

### requirements.txt
- Lists all Python dependencies
- Flask 3.0.0
- openpyxl 3.11.2 (for Excel handling)
- Other Flask dependencies

## Important Notes

### Excel File
The `FX October PnL updated.xlsx` file is included in the container during build. If you need to update it:
1. Replace the file locally
2. Push to repository
3. Trigger a new deployment

### Database
This app doesn't use a database - data is read from Excel files on startup.

### Performance
- First load may take a few seconds (Excel file loading)
- Subsequent operations are instant
- All calculations happen in-memory

## Troubleshooting

### Container won't start
```bash
# Check logs in Dokploy dashboard
# Or run locally with docker-compose up
docker-compose up --build
```

### Port conflicts
Ensure port 5000 is not in use. If needed, modify in docker-compose.yml:
```yaml
ports:
  - "8000:5000"  # Maps 8000 to container's 5000
```

### Excel file not found
Ensure the file path in `app.py` is correct:
```python
calculator = FXProfitCalculator('FX October PnL updated.xlsx')
```

### SSL/HTTPS issues
Dokploy automatically provisions SSL. If issues occur:
1. Wait 5-10 minutes for cert generation
2. Check Dokploy's domain settings
3. Verify DNS records point to Dokploy server

## Deployment Checklist

- [ ] Docker image builds successfully locally
- [ ] Application runs on http://localhost:5000 locally
- [ ] All files pushed to Git repository
- [ ] Dokploy project created
- [ ] Application configured in Dokploy
- [ ] Environment variables set
- [ ] Domain configured with DNS records
- [ ] Deployment triggered and successful
- [ ] App accessible at your domain
- [ ] Both AM and PM sheets working correctly

## Scaling & Maintenance

### Update Application
1. Make changes locally
2. Test with `docker-compose up`
3. Commit and push to repository
4. Trigger new deployment in Dokploy

### Monitor Performance
- Check Dokploy logs for errors
- Monitor CPU and memory usage
- Review application logs

### Backup Excel File
Keep backups of your Excel file:
```bash
git lfs track "*.xlsx"  # Use Git LFS for large files
```

## Support

- Dokploy Docs: https://dokploy.com/docs
- Flask Docs: https://flask.palletsprojects.com/
- Docker Docs: https://docs.docker.com/

## Example Domain Setup

If using domain `myapp.example.com`:

1. **DNS Records:**
   - Type: A
   - Name: myapp
   - Value: Your Dokploy server IP

2. **Dokploy Domain Settings:**
   - Domain: myapp.example.com
   - SSL: Enabled
   - Redirect WWW: Optional

3. **Access Application:**
   - https://myapp.example.com (AM Sheet)
   - https://myapp.example.com/pm (PM Sheet)
