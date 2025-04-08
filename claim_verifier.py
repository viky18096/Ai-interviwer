import requests

def mock_verify_claim(claim):
    # Mock real-time check
    return "No verifiable public data available" if "25%" in claim else "Claim matches publicly available data"
