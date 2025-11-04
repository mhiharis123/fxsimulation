#!/usr/bin/env python
"""
FX Profit Calculator Web App Runner
Run this script to start the web application
"""
import webbrowser
import time
from app import app

if __name__ == '__main__':
    print("Starting FX Profit Calculator Web App...")
    print("Application will be available at http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    time.sleep(1)
    try:
        webbrowser.open('http://localhost:5000')
    except:
        print("Could not open browser automatically. Please visit http://localhost:5000")
    
    app.run(debug=True, port=5000)
