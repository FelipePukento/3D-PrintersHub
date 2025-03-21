<div align="justify">

<!-- Profile -->
<p align="right"><strong><samp><img src = "https://i.pinimg.com/originals/43/3a/88/433a885903b5e6b6b9b5edf681169882.gif" alt="sakura" width="200" height="200"></samp></strong></p>
  <p align="center">
    <samp>
      <b>
        🖨️ Welcome to 3D-PrintersHUB! 🔧
      <br>
        🚀 A simple Python utility to manage a local web-based application.
      </b>
      <br>
        <img src="https://readme-typing-svg.herokuapp.com?font=fira+code&weight=800&size=19&duration=1000&pause=500&color=8C02F7&center=true&vCenter=true&multiline=true&width=600&height=120&lines=This+script+ensures+your+server+is+running;It+automatically+terminates+processes+on+port+5000;Then+it+starts+the+application+and+opens+it+in+your+browser;Scans+port+range+for+available+machines;Identifies+machines+by+MAC+address+and+adds+them+to+the+HUB" alt="Typing SVG" />
      <br>
    </samp>
  </p>
<p align="center" style="display: inline-block;">
    <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/18354dec-cf27-444d-b7ff-3dc17f9e91d8/d900h20-56b3816d-4aa7-40bc-86b6-0a863d26bf8d.gif" width="400" height="300" alt="server">
</p>

<details>
<summary><samp><b>‼️ How It Works ‼️ <img src="https://i.pinimg.com/originals/80/7b/5c/807b5c4b02e765bb4930b7c66662ef4b.gif" width="50" height="50" alt="info"></b></samp></summary>

### Features
- **Checks if port 5000 is in use**: Prevents conflicts by closing any process using the port.
- **Automatically starts `app.py`**: Ensures your web application runs smoothly.
- **Opens the app in your default browser**: Saves you time from manually launching it.
- **Scans a range of ports**: Identifies available machines within a specified range.
- **Detects machines using MAC addresses**: Links machines with active responses (HTTP 200) to the HUB.

### How It Works
1. **Port Check and Termination**:
   - The script scans for active processes using port 5000.
   - If a process is found, it terminates it to free the port.

2. **Starting the Application**:
   - It launches `app.py` as a background process.
   - The script waits a few seconds to ensure the server starts correctly.

3. **Scanning for Available Machines**:
   - It iterates through a predefined port range.
   - For each port, it sends a request and checks for a valid HTTP 200 response.

4. **Identifying Machines by MAC Address**:
   - When a valid machine is found, its MAC address is retrieved.
   - The MAC address is used as a unique identifier to add the machine to the HUB.

5. **Opening the Web Interface**:
   - The script automatically opens the HUB interface in the user's default web browser.

### Printer Setup
- **Same Network Requirement**: All printers must be connected to the same network to be detected.
- **Local Software Service**: Each printer runs a local service that allows communication.
- **Hotspot 2.0 Compatibility**: The system works over Hotspot 2.0 but requires a stable 2.4GHz Wi-Fi network.

### Installation
1. Ensure you have Python installed.
2. Install required dependencies:
   ```sh
   pip install psutil
   ```
3. Place `3D-PrintersHUB.py` and `app.py` in the same directory.

### Usage
Run the script:
```sh
python 3D-PrintersHUB.py
```
Your app will start and automatically open in your browser at `http://localhost:5000`.

### Troubleshooting
- If the script doesn't open the browser, try manually visiting `http://localhost:5000`.
- Ensure `app.py` is correctly configured and executable.
- Check that the scanned ports are within an active range.
- Make sure all printers are on the same 2.4GHz network.

</details>

<details>
<summary><samp><b>📩 Contact 📩</b></samp></summary>

<p align="center">
  <samp>
    You can reach me at [<a href="mailto:friveros@usm.cl">e-mail</a>]
    <br>
    🔵Message me on Discord!🔵 [<a href="https://discord.com/users/788875713604354049">felipe_pukento</a>]
  </samp>
</p>

</details>

</div>
