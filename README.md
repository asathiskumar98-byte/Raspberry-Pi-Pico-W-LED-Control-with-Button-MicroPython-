# 🔘 Raspberry Pi Pico W – LED Control with Button (MicroPython)

This project turns an LED ON when a button is pressed and OFF when released using **MicroPython** on the **Raspberry Pi Pico W**.

---

## 🧰 Requirements
- Raspberry Pi Pico W
- MicroPython firmware installed
- Thonny IDE
- Push button + Jumper wires

---

## ⚙️ Pin Configuration
| Component | Pin | Mode |
|------------|-----|------|
| Onboard LED | "LED" | OUTPUT |
| Button | GPIO16 | INPUT (PULL-UP) |

---

## 🚀 Run the Code
1. Open **Thonny IDE**  
2. Choose Interpreter → *MicroPython (Raspberry Pi Pico)*  
3. Connect Pico W via USB  
4. Copy and save code as `main.py`  
5. Press the button and watch the LED respond instantly 🔆  

---

## 🧩 Concept
The button input uses a **pull-up resistor**, keeping it HIGH until pressed.  
When pressed → logic LOW → LED turns ON.  
When released → logic HIGH → LED turns OFF.  

---

## 🔧 Try These Next
- Add debounce delay: `time.sleep(0.05)`
- Toggle LED on press (instead of hold)
- Use Wi-Fi to control LED via button press status  
