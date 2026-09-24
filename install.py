
#!/usr/bin/env python3
PROJECT_NAME = "Dracula Wireshark All-Rounder"
PROJECT_VERSION = "1.0.0"
RELEASE_DATE = "2026-09-24"

AUTHOR = "Dhruv Meghwal"
AUTHOR_EMAIL = "dhruvmeghwal252009@gmail.com"

GITHUB_USER = "Anonymous-25"
REPOSITORY = "dracula-wireshark"

LICENSE = "MIT"
from pathlib import Path
from datetime import datetime
import subprocess
import sys
# ============================================================
# DRACULA WIRESHARK ALL-ROUNDER INSTALLER
#
# Tested design target:
#   Wireshark 4.6.x
#
# Installs:
#   - Lua protocol helper plugins
#   - Dracula packet coloring rules
#   - Automatic backup
#   - Dracula profile directory
#
# Linux / Unix
# ============================================================


# ============================================================
# SETTINGS
# ============================================================

HOME = Path.home()

# ------------------------------------------------------------
# Wireshark configuration
# ------------------------------------------------------------

WIRESHARK_DIR = (
    HOME
    / ".config"
    / "wireshark"
)

# ------------------------------------------------------------
# Dracula profile
# ------------------------------------------------------------

PROFILE_NAME = "Dracula"

PROFILE_DIR = (
    WIRESHARK_DIR
    / "profiles"
    / PROFILE_NAME
)

# THIS is the important path.
COLORFILTERS = PROFILE_DIR / "colorfilters"

# ------------------------------------------------------------
# Lua plugins
# ------------------------------------------------------------

PLUGIN_DIR = (
    HOME
    / ".local"
    / "lib"
    / "wireshark"
    / "plugins"
)

THEME_DIR = (
    HOME
    / ".local"
    / "lib"
    / "wireshark"
    / "themes"
)

# ------------------------------------------------------------
# Backups
# ------------------------------------------------------------

BACKUP_ROOT = (
    HOME
    / ".local"
    / "share"
    / "dracula-wireshark-backups"
)

TIMESTAMP = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

BACKUP_DIR = (
    BACKUP_ROOT
    / TIMESTAMP
)

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

BACKUP_DIR = BACKUP_ROOT / TIMESTAMP
# ============================================================
# DRACULA PALETTE
# ============================================================

PALETTE = {
    "BG":          "#282A36",
    "CURRENT":     "#44475A",
    "FG":          "#F8F8F2",
    "COMMENT":     "#6272A4",
    "CYAN":        "#8BE9FD",
    "GREEN":       "#50FA7B",
    "ORANGE":      "#FFB86C",
    "PINK":        "#FF79C6",
    "PURPLE":      "#BD93F9",
    "RED":         "#FF5555",
    "YELLOW":      "#F1FA8C",
}


# ============================================================
# DRACULA COLOR PROFILES
#
# Format:
#     foreground, background
#
# Foreground = packet text
# Background = packet row
# ============================================================

DRACULA_COLORS = {

    # --------------------------------------------------------
    # GENERAL
    # --------------------------------------------------------

    "default": (
        PALETTE["FG"],
        PALETTE["BG"],
    ),

    "generic": (
        PALETTE["FG"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # WEB
    # --------------------------------------------------------

    "web": (
        PALETTE["CYAN"],
        PALETTE["BG"],
    ),

    "web_secure": (
        PALETTE["GREEN"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # DNS / DISCOVERY
    # --------------------------------------------------------

    "dns": (
        PALETTE["GREEN"],
        PALETTE["BG"],
    ),

    "discovery": (
        PALETTE["YELLOW"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # TLS / CRYPTO
    # --------------------------------------------------------

    "crypto": (
        PALETTE["PURPLE"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # AUTHENTICATION
    # --------------------------------------------------------

    "authentication": (
        PALETTE["ORANGE"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # EMAIL
    # --------------------------------------------------------

    "email": (
        PALETTE["PINK"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # DATABASE
    # --------------------------------------------------------

    "database": (
        PALETTE["YELLOW"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # REMOTE ACCESS
    # --------------------------------------------------------

    "remote": (
        PALETTE["ORANGE"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # FILE TRANSFER
    # --------------------------------------------------------

    "file_transfer": (
        PALETTE["CYAN"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # NETWORK
    # --------------------------------------------------------

    "network": (
        PALETTE["CYAN"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # ROUTING
    # --------------------------------------------------------

    "routing": (
        PALETTE["PURPLE"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # DIAGNOSTICS
    # --------------------------------------------------------

    "diagnostic": (
        PALETTE["RED"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # WINDOWS / MICROSOFT
    # --------------------------------------------------------

    "windows": (
        PALETTE["CYAN"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # UNIX / LINUX
    # --------------------------------------------------------

    "unix": (
        PALETTE["GREEN"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # VIRTUALIZATION / TUNNELING
    # --------------------------------------------------------

    "virtualization": (
        PALETTE["PURPLE"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # VOIP / REAL-TIME
    # --------------------------------------------------------

    "realtime": (
        PALETTE["PINK"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # WIRELESS
    # --------------------------------------------------------

    "wireless": (
        PALETTE["CYAN"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # USB / HARDWARE
    # --------------------------------------------------------

    "hardware": (
        PALETTE["ORANGE"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # IOT / INDUSTRIAL
    # --------------------------------------------------------

    "iot": (
        PALETTE["YELLOW"],
        PALETTE["CURRENT"],
    ),

    # --------------------------------------------------------
    # SECURITY
    # --------------------------------------------------------

    "security": (
        PALETTE["RED"],
        PALETTE["BG"],
    ),

    # --------------------------------------------------------
    # ERROR / ALERT
    # --------------------------------------------------------

    "error": (
        PALETTE["FG"],
        PALETTE["RED"],
    ),
}


# ============================================================
# PROTOCOL -> COLOR CATEGORY
# ============================================================

PROTOCOL_CATEGORIES = {

    # ========================================================
    # WEB
    # ========================================================

    "http": "web",
    "http2": "web",
    "http3": "web",
    "quic": "web",
    "websocket": "web",

    # ========================================================
    # SECURE WEB / CRYPTO
    # ========================================================

    "tls": "crypto",
    "ssl": "crypto",
    "dtls": "crypto",
    "ocsp": "crypto",

    # ========================================================
    # DNS / DISCOVERY
    # ========================================================

    "dns": "dns",
    "llmnr": "discovery",
    "mdns": "discovery",
    "nbns": "discovery",
    "arp": "discovery",
    "ndp": "discovery",

    # ========================================================
    # DHCP / ADDRESS CONFIGURATION
    # ========================================================

    "dhcp": "network",
    "dhcpv6": "network",

    # ========================================================
    # AUTHENTICATION
    # ========================================================

    "kerberos": "authentication",
    "ntlmssp": "authentication",
    "ntlmv2": "authentication",
    "spnego": "authentication",
    "gss-api": "authentication",
    "radius": "authentication",
    "ldap": "authentication",

    # ========================================================
    # EMAIL
    # ========================================================

    "smtp": "email",
    "smtps": "email",
    "pop": "email",
    "pop3": "email",
    "imap": "email",
    "imap4": "email",

    # ========================================================
    # FILE TRANSFER
    # ========================================================

    "ftp": "file_transfer",
    "ftp-data": "file_transfer",
    "tftp": "file_transfer",
    "sftp": "file_transfer",

    # ========================================================
    # REMOTE ACCESS
    # ========================================================

    "ssh": "remote",
    "telnet": "remote",
    "rdp": "remote",
    "vnc": "remote",
    "winrm": "remote",

    # ========================================================
    # DATABASE
    # ========================================================

    "mysql": "database",
    "pgsql": "database",
    "postgres": "database",
    "mongodb": "database",
    "redis": "database",
    "mssql": "database",
    "tds": "database",

    # ========================================================
    # NETWORK / TRANSPORT
    # ========================================================

    "tcp": "network",
    "udp": "network",
    "sctp": "network",
    "dccp": "network",

    # ========================================================
    # IP
    # ========================================================

    "ip": "network",
    "ipv6": "network",
    "ipsec": "crypto",
    "esp": "crypto",
    "ah": "crypto",

    # ========================================================
    # ROUTING
    # ========================================================

    "bgp": "routing",
    "ospf": "routing",
    "rip": "routing",
    "eigrp": "routing",
    "isis": "routing",
    "hsrp": "routing",
    "vrrp": "routing",

    # ========================================================
    # DIAGNOSTICS
    # ========================================================

    "icmp": "diagnostic",
    "icmpv6": "diagnostic",

    # ========================================================
    # WINDOWS / MICROSOFT
    # ========================================================

    "smb": "windows",
    "smb2": "windows",
    "smb3": "windows",
    "nbss": "windows",
    "msrpc": "windows",
    "dcom": "windows",
    "winreg": "windows",

    # ========================================================
    # UNIX / LINUX
    # ========================================================

    "nfs": "unix",
    "rpc": "unix",
    "sunrpc": "unix",

    # ========================================================
    # VIRTUALIZATION / TUNNELING
    # ========================================================

    "vxlan": "virtualization",
    "geneve": "virtualization",
    "gre": "virtualization",

    # ========================================================
    # VOIP / REAL-TIME
    # ========================================================

    "sip": "realtime",
    "rtp": "realtime",
    "rtcp": "realtime",
    "stun": "realtime",
    "turn": "realtime",
    "turnchannel": "realtime",

    # ========================================================
    # WIRELESS
    # ========================================================

    "wifi": "wireless",
    "wlan": "wireless",
    "btle": "wireless",
    "bluetooth": "wireless",
    "l2cap": "wireless",
    "802.11": "wireless",

    # ========================================================
    # HARDWARE
    # ========================================================

    "usb": "hardware",
    "usbhid": "hardware",
    "usbms": "hardware",

    # ========================================================
    # IOT / INDUSTRIAL
    # ========================================================

    "mqtt": "iot",
    "coap": "iot",
    "modbus": "iot",
    "zwave": "iot",
    "bacnet": "iot",

    # ========================================================
    # SECURITY
    # ========================================================

    "ftp.login": "security",
    "http.authorization": "security",
    "http.cookie": "security",
    "tcp.flags.syn": "security",
    "tcp.flags.fin": "security",
    "tcp.flags.reset": "security",
}


# ============================================================
# RULE STORAGE
# ============================================================

rules = []


# ============================================================
# COLOR HELPERS
# ============================================================

def hex_to_rgb16(hex_color):

    hex_color = hex_color.strip().lstrip("#")

    if len(hex_color) != 6:
        raise ValueError(
            f"Invalid color: #{hex_color}"
        )

    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    except ValueError as exc:
        raise ValueError(
            f"Invalid hexadecimal color: #{hex_color}"
        ) from exc

    # Convert 8-bit -> 16-bit
    return (
        r * 257,
        g * 257,
        b * 257,
    )


def wireshark_rgb(hex_color):
    r, g, b = hex_to_rgb16(hex_color)
    return f"[{r},{g},{b}]"

# ============================================================
# ADD COLORING RULE
# ============================================================

def add_rule(
    name,
    filter_expression,
    foreground=None,
    background=None,
    category=None,
):
    """
    Add a Wireshark packet coloring rule.

    Parameters
    ----------
    name:
        Human-readable Wireshark rule name.

    filter_expression:
        Wireshark display filter.

    foreground:
        Packet text color.

    background:
        Packet row/background color.

    category:
        Dracula color category used when explicit colors
        are not supplied.

    Examples
    --------

    Automatic category:

        add_rule(
            "DRACULA - HTTP",
            "http"
        )

    Explicit colors:

        add_rule(
            "DRACULA - TCP SYN",
            "tcp.flags.syn == 1",
            foreground=PALETTE["RED"],
            background=PALETTE["BG"]
        )

    Explicit category:

        add_rule(
            "DRACULA - DNS",
            "dns",
            category="dns"
        )
    """

    # --------------------------------------------------------
    # Determine colors
    # --------------------------------------------------------

    if foreground is not None or background is not None:

        fg = foreground or PALETTE["FG"]
        bg = background or PALETTE["BG"]

    else:

        if category is None:
            category = PROTOCOL_CATEGORIES.get(
                filter_expression.lower(),
                "default",
            )

        fg, bg = DRACULA_COLORS.get(
            category,
            DRACULA_COLORS["default"],
        )

    # --------------------------------------------------------
    # Convert colors to Wireshark RGB16
    # --------------------------------------------------------

    bg_rgb = wireshark_rgb(bg)
    fg_rgb = wireshark_rgb(fg)

    # --------------------------------------------------------
    # Wireshark colorfilters format
    #
    # @name@filter@[BACKGROUND][FOREGROUND]
    #
    # IMPORTANT:
    # Wireshark expects background FIRST and
    # foreground SECOND.
    # --------------------------------------------------------

    rule = (
        f"@{name}@{filter_expression}@"
        f"{bg_rgb}{fg_rgb}"
    )

    rules.append(rule)

    return rule
add_rule(
    "DRACULA - TCP Analysis Flags",
    "tcp.analysis.flags",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - TCP Retransmission",
    "tcp.analysis.retransmission",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - TCP Fast Retransmission",
    "tcp.analysis.fast_retransmission",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - TCP Spurious Retransmission",
    "tcp.analysis.spurious_retransmission",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - TCP Out Of Order",
    "tcp.analysis.out_of_order",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - TCP Duplicate ACK",
    "tcp.analysis.duplicate_ack",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - TCP Lost Segment",
    "tcp.analysis.lost_segment",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - TCP Previous Segment Lost",
    "tcp.analysis.lost_segment",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - TCP Zero Window",
    "tcp.analysis.zero_window",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - TCP Window Full",
    "tcp.analysis.window_full",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - TCP Keep Alive",
    "tcp.analysis.keep_alive",
    PALETTE["COMMENT"]
)


# ============================================================
# 02 — WEB
# ============================================================

add_rule(
    "DRACULA - HTTP",
    "http",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - HTTP Request",
    "http.request",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - HTTP Response",
    "http.response",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - HTTP2",
    "http2",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - HTTP3",
    "http3",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - WebSocket",
    "websocket",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - QUIC",
    "quic",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - TLS",
    "tls",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - DTLS",
    "dtls",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - OCSP",
    "ocsp",
    PALETTE["PINK"]
)


# ============================================================
# 03 — DNS / NAME RESOLUTION
# ============================================================

add_rule(
    "DRACULA - DNS",
    "dns",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - DNS Query",
    "dns.flags.response == 0",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - DNS Response",
    "dns.flags.response == 1",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - mDNS",
    "mdns",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - LLMNR",
    "llmnr",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - NBNS",
    "nbns",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - SSDP",
    "ssdp",
    PALETTE["GREEN"]
)


# ============================================================
# 04 — DHCP / ADDRESS CONFIGURATION
# ============================================================

add_rule(
    "DRACULA - DHCP",
    "dhcp",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - DHCPv6",
    "dhcpv6",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - BOOTP",
    "bootp",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - ARP",
    "arp",
    PALETTE["YELLOW"]
)



# ============================================================
# 05 — ICMP
# ============================================================

add_rule(
    "DRACULA - ICMP",
    "icmp",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - ICMPv6",
    "icmpv6",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - ICMP Echo",
    "icmp.type == 8",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - ICMP Echo Reply",
    "icmp.type == 0",
    PALETTE["CYAN"]
)


# ============================================================
# 06 — IP
# ============================================================

add_rule(
    "DRACULA - IPv4",
    "ip",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - IPv6",
    "ipv6",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - IPv6 Hop By Hop",
    "ipv6.nxt == 0",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - IP Fragment",
    "ip.flags.mf == 1",
    PALETTE["ORANGE"]
)


# ============================================================
# 07 — TRANSPORT
# ============================================================

add_rule(
    "DRACULA - TCP SYN",
    "tcp.flags.syn == 1 && tcp.flags.ack == 0",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - TCP SYN ACK",
    "tcp.flags.syn == 1 && tcp.flags.ack == 1",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - TCP FIN",
    "tcp.flags.fin == 1",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - TCP RST",
    "tcp.flags.reset == 1",
    PALETTE["RED"]
)


# ============================================================
# 08 — FTP
# ============================================================

add_rule(
    "DRACULA - FTP",
    "ftp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - FTP Data",
    "ftp-data",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - TFTP",
    "tftp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - SFTP",
    "ssh",
    PALETTE["PURPLE"]
)


# ============================================================
# 09 — EMAIL
# ============================================================

add_rule(
    "DRACULA - SMTP",
    "smtp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - SMTP Response",
    "smtp.response",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - IMAP",
    "imap",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - POP",
    "pop",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - MIME",
    "mime_multipart",
    PALETTE["PINK"]
)


# ============================================================
# 10 — REMOTE ACCESS
# ============================================================

add_rule(
    "DRACULA - SSH",
    "ssh",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - Telnet",
    "telnet",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - RDP",
    "rdp",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - VNC",
    "vnc",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - X11",
    "x11",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - SOCKS",
    "socks",
    PALETTE["PURPLE"]
)


# ============================================================
# 11 — WINDOWS / MICROSOFT
# ============================================================

add_rule(
    "DRACULA - SMB",
    "smb",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - SMB2",
    "smb2",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - MSRPC",
    "dcerpc",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - NTLMSSP",
    "ntlmssp",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - Kerberos",
    "kerberos",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - LDAP",
    "ldap",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - LDAPS",
    "ldap && tcp.port == 636",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - MS-WBT",
    "tpkt",
    PALETTE["PINK"]
)


# ============================================================
# 12 — AUTHENTICATION / SECURITY
# ============================================================

add_rule(
    "DRACULA - EAP",
    "eap",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - EAPOL",
    "eapol",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - Kerberos",
    "kerberos",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - NTLM",
    "ntlmssp",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - SPNEGO",
    "spnego",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - GSSAPI",
    "gss-api",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - RADIUS",
    "radius",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - TACACS",
    "tacacs",
    PALETTE["PURPLE"]
)


# ============================================================
# 13 — TIME / MANAGEMENT
# ============================================================

add_rule(
    "DRACULA - NTP",
    "ntp",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - SNMP",
    "snmp",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - Syslog",
    "syslog",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - NetFlow",
    "cflow",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - CFLOW",
    "cflow",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - Diameter",
    "diameter",
    PALETTE["PURPLE"]
)


# ============================================================
# 14 — ROUTING
# ============================================================

add_rule(
    "DRACULA - BGP",
    "bgp",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - OSPF",
    "ospf",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - IS-IS",
    "isis",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - RIP",
    "rip",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - RIPng",
    "ripng",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - VRRP",
    "vrrp",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - HSRP",
    "hsrp",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - LACP",
    "lacp",
    PALETTE["YELLOW"]
)


# ============================================================
# 15 — VLAN / ETHERNET
# ============================================================

add_rule(
    "DRACULA - VLAN",
    "vlan",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - QinQ",
    "vlan && vlan.id",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - STP",
    "stp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - RSTP",
    "stp && stp.version",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - LLDP",
    "lldp",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - CDP",
    "cdp",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - LLMNR",
    "llmnr",
    PALETTE["CYAN"]
)


# ============================================================
# 16 — VPN / TUNNELING
# ============================================================

add_rule(
    "DRACULA - GRE",
    "gre",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - ESP",
    "esp",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - AH",
    "ah",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - IPsec",
    "esp || ah",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - ISAKMP",
    "isakmp",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - ISAKMP",
    "isakmp",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - L2TP",
    "l2tp",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - PPTP",
    "pptp",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - GRE over IPv6",
    "ipv6 && gre",
    PALETTE["PURPLE"]
)


# ============================================================
# 17 — VOIP / MEDIA
# ============================================================

add_rule(
    "DRACULA - SIP",
    "sip",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - SIP Response",
    "sip.Status-Code",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - SDP",
    "sdp",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - RTP",
    "rtp",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - RTCP",
    "rtcp",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - RTSP",
    "rtsp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - MGCP",
    "mgcp",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - H323",
    "h225 || h245",
    PALETTE["PURPLE"]
)


# ============================================================
# 18 — IoT / MESSAGING
# ============================================================

add_rule(
    "DRACULA - MQTT",
    "mqtt",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - CoAP",
    "coap",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - AMQP",
    "amqp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - XMPP",
    "xmpp",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - WebRTC STUN",
    "stun",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - TURN",
    "turnchannel",
    PALETTE["PURPLE"]
)


# ============================================================
# 19 — DATABASES
# ============================================================

add_rule(
    "DRACULA - MySQL",
    "mysql",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - PostgreSQL",
    "pgsql",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - TDS",
    "tds",
    PALETTE["PURPLE"]
)


# ============================================================
# 20 — DIRECTORY / FILE SERVICES
# ============================================================

add_rule(
    "DRACULA - NFS",
    "nfs",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - RPC",
    "rpc",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - AFP",
    "afp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - iSCSI",
    "iscsi",
    PALETTE["PURPLE"]
)


# ============================================================
# 21 — CONTAINERS / VIRTUALIZATION
# ============================================================

add_rule(
    "DRACULA - VXLAN",
    "vxlan",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - GTP",
    "gtp",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - Geneve",
    "geneve",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - GRE",
    "gre",
    PALETTE["PURPLE"]
)


# ============================================================
# 22 — WIRELESS
# ============================================================

add_rule(
    "DRACULA - 802.11",
    "wlan",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - 802.11 Management",
    "wlan.fc.type == 0",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - 802.11 Control",
    "wlan.fc.type == 1",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - 802.11 Data",
    "wlan.fc.type == 2",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - EAPOL",
    "eapol",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - ZigBee",
    "zbee_nwk",
    PALETTE["GREEN"]
)


# ============================================================
# 23 — BLUETOOTH
# ============================================================

add_rule(
    "DRACULA - Bluetooth",
    "bluetooth",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - Bluetooth LE",
    "btle",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - Bluetooth L2CAP",
    "btl2cap",
    PALETTE["PINK"]
)


# ============================================================
# 24 — USB / HARDWARE
# ============================================================

add_rule(
    "DRACULA - USB",
    "usb",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - USB HID",
    "usbhid",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - USB Mass Storage",
    "usbms",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - CAN",
    "can",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - LIN",
    "lin",
    PALETTE["ORANGE"]
)


# ============================================================
# 25 — INDUSTRIAL / OT
# ============================================================

add_rule(
    "DRACULA - Modbus",
    "modbus",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - DNP3",
    "dnp3",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - Profinet",
    "pn_io",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - EtherNet/IP",
    "enip",
    PALETTE["CYAN"]
)


# ============================================================
# 26 — NETWORK MANAGEMENT / DISCOVERY
# ============================================================

add_rule(
    "DRACULA - ICMP Router",
    "icmp",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - CDP",
    "cdp",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - LLDP",
    "lldp",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - VRRP",
    "vrrp",
    PALETTE["YELLOW"]
)

add_rule(
    "DRACULA - HSRP",
    "hsrp",
    PALETTE["YELLOW"]
)


# ============================================================
# 27 — NETWORK STORAGE
# ============================================================

add_rule(
    "DRACULA - iSCSI",
    "iscsi",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - NFS",
    "nfs",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - Fibre Channel",
    "fc",
    PALETTE["CYAN"]
)


# ============================================================
# 28 — RPC / DISTRIBUTED SYSTEMS
# ============================================================

add_rule(
    "DRACULA - ONC RPC",
    "rpc",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - DCE RPC",
    "dcerpc",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - JSON",
    "json",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - XML",
    "xml",
    PALETTE["CYAN"]
)


# ============================================================
# 29 — AUTH / APPLICATION SECURITY
# ============================================================

add_rule(
    "DRACULA - HTTP Authorization",
    "http.authorization",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - HTTP Cookie",
    "http.cookie",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - HTTP Credentials",
    "http.authbasic",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - TLS Alert",
    "tls.alert_message",
    PALETTE["RED"]
)

add_rule(
    "DRACULA - TLS Handshake",
    "tls.handshake",
    PALETTE["PURPLE"]
)


# ============================================================
# 30 — STREAM / SESSION PROTOCOLS
# ============================================================

add_rule(
    "DRACULA - SCTP",
    "sctp",
    PALETTE["CYAN"]
)

add_rule(
    "DRACULA - DCCP",
    "dccp",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - UDPLite",
    "udplite",
    PALETTE["ORANGE"]
)


# ============================================================
# 31 — GENERIC APPLICATION PROTOCOLS
# ============================================================

add_rule(
    "DRACULA - IRC",
    "irc",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - NNTP",
    "nntp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - Gopher",
    "gopher",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - Finger",
    "finger",
    PALETTE["COMMENT"]
)

add_rule(
    "DRACULA - Daytime",
    "daytime",
    PALETTE["COMMENT"]
)

add_rule(
    "DRACULA - Chargen",
    "chargen",
    PALETTE["COMMENT"]
)


# ============================================================
# 32 — NETWORK CONTROL
# ============================================================

add_rule(
    "DRACULA - IGMP",
    "igmp",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - MLD",
    "icmpv6.type == 130",
    PALETTE["GREEN"]
)

add_rule(
    "DRACULA - PIM",
    "pim",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - RSVP",
    "rsvp",
    PALETTE["ORANGE"]
)


# ============================================================
# 33 — GENERIC NETWORK PROTOCOLS
# ============================================================

add_rule(
    "DRACULA - IPsec",
    "esp",
    PALETTE["PINK"]
)

add_rule(
    "DRACULA - MPLS",
    "mpls",
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - PPP",
    "ppp",
    PALETTE["ORANGE"]
)

add_rule(
    "DRACULA - GRE",
    "gre",
    PALETTE["PURPLE"]
)


# ============================================================
# 34 — GENERIC TCP / UDP FALLBACK
# ============================================================
#
# IMPORTANT:
# These MUST remain near the bottom.
#
# Any known protocol above them gets its own color first.
#

add_rule(
    "DRACULA - TCP",
    "tcp",
    PALETTE["CURRENT"],
    PALETTE["FG"]
)

add_rule(
    "DRACULA - UDP",
    "udp",
    PALETTE["CURRENT"],
    PALETTE["FG"]
)


# ============================================================
# 35 — IP FALLBACK
# ============================================================

add_rule(
    "DRACULA - IPv6 Fallback",
    "ipv6",
    PALETTE["BG"],
    PALETTE["PURPLE"]
)

add_rule(
    "DRACULA - IPv4 Fallback",
    "ip",
    PALETTE["BG"],
    PALETTE["CYAN"]
)


# ============================================================
# 36 — ETHERNET FALLBACK
# ============================================================

add_rule(
    "DRACULA - Ethernet",
    "eth",
    PALETTE["BG"],
    PALETTE["FG"]
)

# ============================================================
# WRITE COLORFILTERS
# ============================================================

COLORFILTERS = PROFILE_DIR / "colorfilters"

print()
print("[*] Installing Dracula coloring rules...")

COLORFILTERS.write_text(
    "\n".join(rules) + "\n",
    encoding="utf-8"
)

print(
    f"[+] Installed {len(rules)} coloring rules"
)


# ============================================================
# OPTIONAL WIRESHARK PROFILE INFO
# ============================================================
# ============================================================
# PROJECT METADATA
# ============================================================

PROJECT_NAME = "Dracula Wireshark All-Rounder"
PROJECT_VERSION = "1.0.0"

AUTHOR = "Dhruv Meghwal"
GITHUB = "https://github.com/Anonymous-25"
LICENSE = "MIT"

CONTRIBUTORS = [
    "Dhruv Meghwal <dhruvmeghwal252009@gmail.com>",
]

SUPPORTED_WIRESHARK = "4.6.x"
SUPPORTED_OS = "Linux / Windows / macOS"

PROFILE_INFO = PROFILE_DIR / "dracula_profile.txt"

PROFILE_INFO.write_text(
f"""
==============================================================
{PROJECT_NAME}
==============================================================

Version
-------
{PROJECT_VERSION}

Generated
---------
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Author
------
{AUTHOR}

GitHub
------
{GITHUB}

License
-------
{LICENSE}

Contributors
------------
{chr(10).join(CONTRIBUTORS)}

Compatibility
-------------
Wireshark : {SUPPORTED_WIRESHARK}
Platforms : {SUPPORTED_OS}

Installation Paths
------------------
Profile Directory :
{PROFILE_DIR}

Lua Plugins :
{PLUGIN_DIR}

Color Filters :
{COLORFILTERS}

Statistics
----------
Installed Rules : {len(rules)}
Lua Plugins     : {len(list(PLUGIN_DIR.glob("*.lua")))}

Dracula Palette
---------------
Background   : {PALETTE["BG"]}
Current Line : {PALETTE["CURRENT"]}
Foreground   : {PALETTE["FG"]}
Comment      : {PALETTE["COMMENT"]}
Cyan         : {PALETTE["CYAN"]}
Green        : {PALETTE["GREEN"]}
Orange       : {PALETTE["ORANGE"]}
Pink         : {PALETTE["PINK"]}
Purple       : {PALETTE["PURPLE"]}
Red          : {PALETTE["RED"]}
Yellow       : {PALETTE["YELLOW"]}

Project Notes
-------------
This profile provides protocol-aware coloring rules
for Wireshark using the Dracula color palette.

Rules are community-maintained and may expand
through future releases and GitHub contributions.

==============================================================
""".strip() + "\n",
encoding="utf-8"
)
# ============================================================
# CHECK WIRESHARK
# ============================================================

print()
print("[*] Checking Wireshark installation...")
try:

    result = subprocess.run(
        [
            "wireshark",
            "--version"
        ],
        capture_output=True,
        text=True,
        timeout=5
    )

    if result.returncode == 0:

        first_line = (
            result.stdout.strip()
            .splitlines()[0]
            if result.stdout.strip()
            else "Wireshark detected"
        )

        print(
            f"[+] {first_line}"
        )

    else:

        print(
            "[!] Wireshark command returned an error."
        )

except FileNotFoundError:

    print(
        "[!] Wireshark executable was not found in PATH."
    )

except Exception as exc:

    print(
        f"[!] Version check failed: {exc}"
    )


# ============================================================
# FINISHED
# ============================================================
print()
print("=" * 72)
print(f" {PROJECT_NAME} v{PROJECT_VERSION}")
print("=" * 72)

print()
print("Installation Summary")
print("--------------------")
print(f"Profile Directory : {PROFILE_DIR}")
print(f"Lua Plugins       : {PLUGIN_DIR}")
print(f"Color Filters     : {COLORFILTERS}")
print(f"Backup Directory  : {BACKUP_DIR}")

print()
print("Statistics")
print("----------")
print(f"Installed Rules   : {len(rules)}")

print()
print("Compatibility")
print("-------------")
print(f"Wireshark         : {SUPPORTED_WIRESHARK}")

print()
print("Next Steps")
print("----------")
print("1. Close Wireshark completely.")
print("2. Launch Wireshark.")
print("3. Open View → Coloring Rules.")
print("4. Verify Dracula rules are loaded.")
print("5. For Lua changes use:")
print("     Analyze → Reload Lua Plugins")

print()
print("Project")
print("-------")
print(f"Author           : {AUTHOR}")
print(f"License          : {LICENSE}")
print(f"Repository       : {GITHUB}")

print()
print("=" * 72)
print(" Installation completed successfully.")
print("=" * 72)
print()
# ============================================================
# VERIFY COLORFILTERS
# ============================================================

print()
print("[*] Verifying colorfilters...")

if not COLORFILTERS.exists():

    print(
        "[!] ERROR: colorfilters was not created."
    )

    sys.exit(1)

installed_rules = 0

for line in COLORFILTERS.read_text(
    encoding="utf-8",
    errors="ignore"
).splitlines():

    if line.startswith("@"):

        installed_rules += 1

print(
    f"[+] File contains {installed_rules} rules"
)

if installed_rules != len(rules):

    print(
        "[!] WARNING: Rule count mismatch!"
    )

    print(
        f"    Python rules : {len(rules)}"
    )

    print(
        f"    File rules   : {installed_rules}"
    )

else:

    print(
        "[✓] Rule count verified."
    )