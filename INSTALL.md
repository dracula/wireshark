# Install

## Requirements

* Wireshark 4.x
* Python 3.10+

## Installation

Clone the repository:

```bash
git clone https://github.com/Anonymous-25/dracula-wireshark.git

cd dracula-wireshark
```

Run the installer:

```bash
python3 install.py
```

The installer will:

* Create the Dracula profile
* Install coloring rules
* Generate profile metadata
* Create backups when needed

## Verify Installation

1. Start Wireshark
2. Open:

```text
View → Coloring Rules
```

3. Select the Dracula profile
4. Open a capture file and verify protocol coloring

## Updating

Pull the latest changes:

```bash
git pull
```

Then rerun:

```bash
python3 install.py
```

## Troubleshooting

### Invalid Protocol Errors

Check whether the protocol exists in your Wireshark build:

```bash
tshark -G protocols
```

Check available fields:

```bash
tshark -G fields
```

### Reset Profile

Remove the generated profile and reinstall:

```bash
rm -rf ~/.config/wireshark/profiles/Dracula
python3 install.py
```
