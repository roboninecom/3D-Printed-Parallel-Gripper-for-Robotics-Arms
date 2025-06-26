# Technical Specifications

## Mechanical Specifications

### Overall Dimensions
- **Length**: ~150mm (rod length)
- **Width**: ~80mm (approximate frame width)
- **Height**: ~60mm (approximate frame height)
- **Weight**: ~200-300g (depending on infill and material)

### Gripper Performance
- **Maximum Opening**: Determined by rod length and gear ratio
- **Closing Force**: Servo-dependent (STS3215: ~15kg·cm torque)
- **Positioning Accuracy**: ±0.1° (servo resolution: 4096 positions/360°)
- **Speed**: Configurable, default 4800 units (adjustable in software)
- **Repeatability**: ±0.05° (typical for STS3215)

### Materials
- **3D Printed Parts**: PLA, PETG, ABS, or Nylon
- **Linear Rods**: Stainless steel 6mm diameter
- **Bearings**: Steel with lubrication
- **Fasteners**: Stainless steel (recommended)

## Electrical Specifications

### Servo Motor (Feetech STS3215)
- **Operating Voltage**: 6.0-12.6V DC
- **Current Draw**: 
  - Idle: ~100mA
  - Operating: 500-1500mA (load dependent)
  - Stall: ~2500mA (maximum)
- **Communication**: TTL/RS485 serial
- **Baud Rate**: Up to 1,000,000 bps
- **Protocol**: Feetech STS protocol
- **Position Resolution**: 4096 positions (0.088°/step)
- **Speed Range**: 0-2875 RPM
- **Torque**: 15kg·cm @ 12V

### Communication Interface
- **Protocol**: Custom Feetech STS protocol
- **Data Format**: 8N1 (8 data bits, no parity, 1 stop bit)
- **Flow Control**: None
- **Cable**: 4-wire (VCC, GND, DATA+, DATA-)
- **Connector**: JST or similar (servo dependent)

## Environmental Specifications

### Operating Conditions
- **Temperature Range**: -10°C to +50°C
- **Humidity**: 0-85% RH (non-condensing)
- **Altitude**: Up to 2000m
- **Vibration**: Light industrial environments

### Storage Conditions
- **Temperature Range**: -20°C to +60°C
- **Humidity**: 0-95% RH (non-condensing)

## Performance Characteristics

### Positioning
- **Resolution**: 0.088° per step (4096 steps/360°)
- **Accuracy**: ±0.1° (typical)
- **Repeatability**: ±0.05° (typical)
- **Backlash**: <0.2° (mechanical)

### Speed and Acceleration
- **Maximum Speed**: Configurable (default: 4800 units)
- **Acceleration**: Configurable (default: 5 units)
- **Response Time**: <100ms for small movements
- **Settling Time**: <500ms (typical)

### Force and Torque
- **Grip Force**: Depends on gear ratio and servo torque
- **Holding Force**: Full servo torque available
- **Maximum Load**: Limited by servo specifications

## Monitoring and Feedback

### Real-time Data Available
- **Position**: Current angular position (0-4095)
- **Speed**: Current rotational speed
- **Load**: Current load percentage (0-100%)
- **Temperature**: Servo internal temperature (°C)
- **Voltage**: Supply voltage (V)
- **Current**: Motor current draw (mA)

### Error Detection
- **Overload Protection**: Automatic shutdown on excessive load
- **Overtemperature Protection**: Thermal shutdown
- **Position Error Detection**: Deviation from target position
- **Communication Error Detection**: Protocol-level error checking

## Compliance and Standards

### Safety
- **Low Voltage**: Operates at safe voltage levels (<15V)
- **Mechanical Safety**: Rounded edges, no pinch points in normal operation
- **Electrical Safety**: Proper grounding and isolation recommended

### EMC (Electromagnetic Compatibility)
- **Emissions**: Low-level digital signals
- **Immunity**: Standard industrial levels
- **Recommendations**: Proper cable shielding for noisy environments

## Mounting and Integration

### Mounting Options
- **Robot Arm Interface**: Custom adapter plate required
- **Mounting Holes**: M4 or M5 (depending on design)
- **Orientation**: Any orientation supported
- **Cable Management**: Strain relief recommended

### Integration Requirements
- **Control System**: Any system supporting serial communication
- **Power Supply**: 6-12V DC, minimum 3A capacity
- **Communication**: TTL or RS485 interface
- **Software**: Python library provided, other languages possible

## Maintenance Requirements

### Regular Maintenance
- **Visual Inspection**: Monthly check for wear or damage
- **Screw Tightness**: Check quarterly
- **Bearing Lubrication**: Annual or as needed
- **Cable Inspection**: Check for wear or damage

### Replacement Parts
- **Bearings**: Standard sizes, readily available
- **Fasteners**: Standard metric screws
- **3D Printed Parts**: Can be reprinted as needed
- **Servo**: Feetech STS3215 or compatible

### Troubleshooting
- **Position Errors**: Check mechanical alignment
- **Communication Errors**: Verify connections and baud rate
- **Overheating**: Check load and duty cycle
- **Mechanical Binding**: Inspect bearings and alignment

---

**Specifications subject to change based on actual implementation and testing** 