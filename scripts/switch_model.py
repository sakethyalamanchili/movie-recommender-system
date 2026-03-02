"""Trigger model hot-swap on the live API.

Usage:
    python scripts/switch_model.py --api-url https://your-service.run.app --model v1.2
"""

import argparse
import os
import requests


def switch(api_url: str, model_version: str, token: str):
    resp = requests.post(
        f"{api_url}/switch",
        params={"model": model_version},
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.json()}")
    return resp.ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-url", default=os.getenv("API_URL", "http://localhost:8000"))
    parser.add_argument("--model", required=True, help="Model version to switch to")
    parser.add_argument("--token", default=os.getenv("ADMIN_TOKEN", ""))
    args = parser.parse_args()
    switch(args.api_url, args.model, args.token)
