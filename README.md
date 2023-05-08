# Alert Maintenance Sakura VPS IP

This script sends an email alert if a specified IP address is found in the Sakura VPS maintenance information within the last 24 hours. It fetches the maintenance information from an RSS feed, checks the content for target IP addresses, and sends an email using a local mailer (127.0.0.1) if any matching IP addresses are found. This project is a collaboration with OpenAI's GPT-4.

## Requirements

- Python 3.6 or later
- requests
- beautifulsoup4
- feedparser

## Installation

1. Clone the repository:  
git clone https://github.com/yourusername/alert_maintenance_sakura_vps_ip.git  
cd alert_maintenance_sakura_vps_ip

2. Install the required packages (if required):  
pip install -r requirements.txt

## Usage

1. Open `alert_maintenance_sakura_vps_ip.py` and update the following configurations with your desired values:  
 - `rss_url`: The RSS URL for the Sakura VPS maintenance information
 - `target_ips`: A list of target IP addresses
 - `sender_address`: The sender's email address
 - `to_address`: The recipient's email address

2. Run the script:  
python alert_maintenance_sakura_vps_ip.py


The script will check the maintenance information from the last 24 hours for the target IP addresses and send an email alert using a local mailer (127.0.0.1) if any matches are found.

## License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See the [LICENSE](LICENSE) file for details.
