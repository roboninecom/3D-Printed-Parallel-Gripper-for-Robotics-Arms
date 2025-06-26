# Quick Start Guide

Get your parallel gripper up and running in 30 minutes!

## 🎥 See the Final Result
Before you start, check out the [working gripper in action](https://youtube.com/shorts/Ss4TbO_psto?si=v6VbK91Q2vyNlbNd) to see what you'll be building!

## What You'll Need

### Hardware
- [ ] All 3D printed parts (see [3D Models](../hardware/3d-models/))
- [ ] Electronic components (see [BOM](bom.md))
- [ ] Mechanical components (bearings, rods, fasteners)
- [ ] Tools (screwdrivers, hex keys)

### Software
- [ ] Python 3.6+ installed
- [ ] STServo SDK downloaded
- [ ] Serial communication interface

## Step 1: 3D Print the Parts (2-4 hours)

1. Download STL files from `hardware/3d-models/`
2. Print with recommended settings:
   - Layer height: 0.2mm
   - Infill: 20% (frame/clamps), 30% (gears)
   - Material: PLA or PETG
3. Remove supports and test-fit bearings

## Step 2: Gather Components (1-2 days shipping)

Order parts from the [Bill of Materials](bom.md):
- Feetech STS3215 servo
- Waveshare bus servo adapter
- Bearings (2x MR106ZZ, 4x LM6UU)
- Steel rods (2x 6mm x 150mm)
- Fasteners (M3, M4 screws and nuts)

## Step 3: Assembly (30 minutes)

Follow the detailed [Assembly Guide](assembly-guide.md):

1. **Install bearings** in clamps (5 min)
2. **Mount gear** to servo (5 min)
3. **Attach servo** to main frame (5 min)
4. **Install frame bearings** (5 min)
5. **Add rods and clamps** (5 min)
6. **Attach gear racks** (5 min)

## Step 4: Software Setup (10 minutes)

1. **Install STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **Configure connection**
   Edit `software/python/gripper_control.py`:
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID
   ```

## Step 5: First Test (5 minutes)

1. **Connect hardware**
   - Servo to bus adapter
   - Bus adapter to computer
   - Power supply (6-12V)

2. **Run basic test**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **Try basic commands**
   - Enter `45` to open gripper
   - Enter `-45` to close gripper
   - Enter `0` to center
   - Press Enter to exit

## Step 6: Run Examples (5 minutes)

```bash
cd examples
python basic_usage.py
```

## Troubleshooting

### Connection Issues
- ✅ Check COM port in Device Manager (Windows)
- ✅ Verify servo power LED
- ✅ Try different baud rates
- ✅ Check cable connections

### Movement Issues
- ✅ Verify gear engagement
- ✅ Check for mechanical binding
- ✅ Ensure bearings move freely
- ✅ Monitor servo temperature

### Software Issues
- ✅ Install STServo SDK correctly
- ✅ Check Python version (3.6+)
- ✅ Verify serial port permissions (Linux)

## Next Steps

🎉 **Congratulations!** Your gripper is working!

Now you can:
- Integrate with your robot arm
- Modify the control software
- Create custom applications
- Share your projects with the community

## Need Help?

- 📖 Read the [full documentation](../README.md)
- 🐛 Report issues on GitHub
- 💬 Join community discussions
- 📧 Contact the maintainers

---

**Welcome to the parallel gripper community!** 🤖 