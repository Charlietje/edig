# edig

Extended dig script.
Show the relevant DNS records of a domain or IP.
Domain can be domain or url.

## DNS lookup
edig https://google.com/test

```
SOA
     ns1.google.com.

NS
     google.com. 345600 IN NS ns3.google.com.
     google.com. 345600 IN NS ns2.google.com.
     google.com. 345600 IN NS ns4.google.com.
     google.com. 345600 IN NS ns1.google.com.

A
     google.com. 196 IN A 216.58.215.46

PTR
     46.215.58.216.in-addr.arpa. 86400 IN PTR par21s17-in-f14.1e100.net.

TXT
     google.com. 300 IN TXT "globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8="
     google.com. 300 IN TXT "v=spf1 include:_spf.google.com ~all"
     google.com. 300 IN TXT "docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e"
     google.com. 300 IN TXT "facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95"
     google.com. 300 IN TXT "docusign=1b0a6754-49b1-4db5-8540-d2c12664b289"

MX
     google.com. 600 IN MX 50 alt4.aspmx.l.google.com.
     google.com. 600 IN MX 10 aspmx.l.google.com.
     google.com. 600 IN MX 30 alt2.aspmx.l.google.com.
     google.com. 600 IN MX 20 alt1.aspmx.l.google.com.
     google.com. 600 IN MX 40 alt3.aspmx.l.google.com.

WHOIS
     description:  GOOGLE, US
     netname    :  GOOGLE

REDIRECT
     301 => http://google.com/
     200 => http://www.google.com/
```

## PTR lookup with geoip
edig 216.58.215.46
```
PTR
     46.215.58.216.in-addr.arpa. 86196 IN PTR par21s17-in-f14.1e100.net.

GEOIP
     United States

WHOIS
     description:  GOOGLE, US
     netname    :  GOOGLE
```
