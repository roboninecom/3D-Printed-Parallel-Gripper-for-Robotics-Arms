# Examples - Parallel Gripper

This directory contains example code demonstrating how to use the parallel gripper in various scenarios.

## Available Examples

### `basic_usage.py`
Demonstrates fundamental gripper operations:
- Connecting to the gripper
- Moving to specific positions
- Reading status information
- Basic error handling

**Usage:**
```bash
cd examples
python basic_usage.py
```

## Configuration

Before running examples, you may need to adjust configuration parameters:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

## Common Issues

### Connection Problems
- **Windows**: Check Device Manager for correct COM port
- **Linux**: Ensure user has access to serial ports (`sudo usermod -a -G dialout $USER`)
- **macOS**: Use `/dev/cu.usbserial-*` or `/dev/tty.usbserial-*`

### Permission Errors
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

### STServo SDK Issues
Make sure the STServo SDK is properly installed:
1. Download from: [STServo Python SDK](https://files.waveshare.com/wiki/Bus-Servo-Adapter-(A)/STServo_Python.zip)
2. Extract the downloaded ZIP file and copy the `STservo_sdk` folder (with the folder itself) to `software/python/` directory

## Creating Your Own Examples

When creating new examples:

1. **Import the gripper module**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **Handle errors gracefully**
   ```python
   try:
       gripper = ParallelGripper()
       if not gripper.connect():
           print("Connection failed!")
           return
       # Your code here
   finally:
       gripper.disconnect()
   ```

3. **Include proper documentation**
   - Clear description of what the example does
   - Required hardware setup
   - Expected behavior

## Safety Notes

⚠️ **Important Safety Considerations:**
- Always monitor temperature and current draw
- Implement proper error handling
- Test with low forces first
- Ensure proper mechanical setup
- Keep fingers clear of moving parts

## Contributing Examples

We welcome new examples! Please:
- Follow the existing code style
- Include comprehensive comments
- Test thoroughly before submitting
- Add entry to this README

---

**Happy coding!** 🤖 