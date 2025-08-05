import winreg  # Built-in for live Windows registry access
import requests  # For querying external APIs like MITRE or CVE
from reportlab.lib.pagesizes import letter  # PDF page size
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table  # PDF elements
from reportlab.lib.styles import getSampleStyleSheet  # PDF styling

# Common registry paths prone to malware (persistence, services, etc.)
COMMON_KEYS = [
    r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run',  # Autorun programs
    r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce',  # One-time runs
    r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run',  # User-specific autoruns
    r'HKLM\SYSTEM\CurrentControlSet\Services',  # System services (often hijacked)
    # Add more as needed, e.g., AppInit_DLLs for DLL injection
]