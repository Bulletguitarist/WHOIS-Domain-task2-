import whois
import csv
import os
from datetime import datetime

# Create results folder if not exists
os.makedirs("results", exist_ok=True)

def clean_date(date_value):
    """
    WHOIS sometimes returns list of dates.
    This function converts it to YYYY-MM-DD string.
    """
    if isinstance(date_value, list):
        date_value = date_value[0]

    if hasattr(date_value, "strftime"):
        return date_value.strftime("%Y-%m-%d")

    return "N/A"


def get_domain_info(domain):
    try:
        w = whois.whois(domain)

        data = {
            "Domain": domain,
            "Registrar": w.registrar if w.registrar else "N/A",
            "Creation Date": clean_date(w.creation_date),
            "Expiry Date": clean_date(w.expiration_date),
            "Name Servers": ", ".join(w.name_servers) if w.name_servers else "N/A"
        }

        return data

    except Exception as e:
        print(f"[ERROR] WHOIS lookup failed: {e}")
        return None


def save_to_txt(data):
    filename = f"results/{data['Domain']}_whois.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
    print(f"[+] TXT saved: {filename}")


def save_to_csv(data):
    filename = "results/whois_results.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

    print(f"[+] CSV updated: {filename}")


if __name__ == "__main__":
    print("=== WHOIS DOMAIN INFO CHECKER ===")
    domain = input("Enter domain (example: google.com): ").strip()

    info = get_domain_info(domain)

    if info:
        print("\n--- WHOIS INFORMATION ---")
        for k, v in info.items():
            print(f"{k}: {v}")

        save_to_txt(info)
        save_to_csv(info)
    else:
        print("No data saved due to error.")
