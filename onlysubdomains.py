import dns.resolver

def get_possible_subdomains(domain):
    subdomains = []
    with open("subdomains.txt") as f:
        subdomains = [line.strip() + "." + domain for line in f]
    print(f"[+] Possible subdomains for {domain}:")
    for subdomain in subdomains:
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            print(f"  {subdomain}")
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            pass
            

if __name__ == '__main__':
    domain = input("Enter a domain name: ")
    get_possible_subdomains(domain)
