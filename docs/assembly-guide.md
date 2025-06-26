# Assembly Guide

## Overview

This guide provides step-by-step instructions for assembling the parallel gripper. Follow these steps carefully to ensure proper operation.

## Required Tools

- Phillips head screwdriver
- Hex key set (M3, M4)
- Small pliers (for handling bearings)

## Safety Precautions

- Handle bearings carefully to avoid contamination
- Ensure all screws are properly tightened but not over-torqued
- Test servo operation before final assembly

## Assembly Steps

### Step 1: Install Linear Bearings in Clamps

**Components needed:**
- 2x Clamps (RB9.01.060.020)
- 4x LM6UU Linear Bearings (12x6x19 mm)

**Instructions:**
1. Take the first clamp part
2. Carefully press 2x LM6UU bearings into the designated bearing seats
3. Ensure bearings are fully seated and can rotate freely
4. Repeat for the second clamp
5. **Note**: Bearings should slide smoothly without binding

### Step 2: Prepare Servo and Drive Gear

**Components needed:**
- 1x Feetech STS3215 Servo
- 1x Drive Gear (RB9.01.060.040)
- 1x Servo disk (from servo kit)
- 1x Servo mounting screw (from servo kit)

**Instructions:**
1. Insert the Drive Gear into the servo disk from the servo kit
2. Align the gear teeth properly with the disk
3. Mount the gear assembly onto the servo output shaft
4. Secure with the screw provided in the servo kit
5. **Important**: Ensure the gear is properly aligned and rotates smoothly

### Step 3: Mount Servo to Main Frame

**Components needed:**
- 1x Main Frame (RB9.01.060.010)
- 1x Assembled servo with gear
- 4x Self-tapping screws (from servo kit)

**Instructions:**
1. Position the servo in the designated mounting area on the main frame
2. Align the servo mounting holes with the frame
3. Secure the servo using 4x self-tapping screws from the servo kit
4. **Check**: Servo should be firmly mounted with no play

### Step 4: Install Main Frame Bearings

**Components needed:**
- 2x MR106ZZ Bearings (10x6x3 mm)
- 2x M4x8 DIN 7991 screws

**Instructions:**
1. Insert the 2x MR106ZZ bearings into their designated positions on the main frame
2. These bearings will guide the linear rods
3. Secure each bearing with 1x M4x8 screw
4. **Note**: Do not over-tighten; bearings should rotate freely

### Step 5: Install Rods and Clamps

**Components needed:**
- 2x Stainless Steel Rods (6mm diameter, 150mm length)
- 2x Assembled clamps (with LM6UU bearings)
- 4x M3x20 DIN 7991 screws
- 4x M3 DIN 934 nuts

**Instructions:**
1. Insert the 2x steel rods through the main frame bearings
2. Slide the 2x clamps onto the rods (LM6UU bearings should slide smoothly)
3. Position the clamps symmetrically from the center of the main frame
4. Secure each clamp to the rods using 2x M3x20 screws and 2x M3 nuts per clamp
5. **Critical**: Ensure clamps move smoothly along the rods

### Step 6: Attach Gear Racks

**Components needed:**
- 2x Gear Racks (RB9.01.060.030)
- 4x M3x10 DIN 7991 screws

**Instructions:**
1. Position the gear racks on the back side of each clamp
2. **Important**: Ensure clamps remain symmetrically positioned from the main frame center
3. The gear racks should engage properly with the drive gear
4. Secure each gear rack with 2x M3x10 screws
5. **Test**: Manually rotate the servo to verify smooth gear engagement

## Final Checks

### Mechanical Verification
- [ ] All screws are properly tightened
- [ ] Clamps move smoothly along the rods
- [ ] Gear engagement is smooth without binding
- [ ] No excessive play in any joints
- [ ] Bearings rotate freely

### Electrical Connection
- [ ] Servo connector is properly seated
- [ ] Bus servo adapter is connected
- [ ] Power supply is appropriate (6-12V DC)

### Functional Test
1. Connect the servo to your control system
2. Run the test software to verify operation
3. Check for smooth movement and proper positioning
4. Monitor servo feedback (current, temperature, load)

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|----------------|----------|
| Clamps bind on rods | Misaligned bearings | Check LM6UU bearing installation |
| Gear noise/binding | Poor gear engagement | Adjust gear rack position |
| Servo errors | Electrical connection | Verify wiring and power supply |
| Uneven movement | Asymmetric assembly | Check clamp positioning |

## Maintenance

- **Regular**: Check screw tightness
- **Monthly**: Clean and lubricate bearings if needed
- **As needed**: Monitor servo temperature and current draw

---

**Assembly Complete!** Your parallel gripper is now ready for integration and testing. 