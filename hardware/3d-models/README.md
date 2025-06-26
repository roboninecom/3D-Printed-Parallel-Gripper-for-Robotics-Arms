# 3D Models - Parallel Gripper

This directory contains all the STL files needed to 3D print the parallel gripper components.

## Files

| File | Part Number | Description | Quantity | Notes |
|------|-------------|-------------|----------|-------|
| `main-frame.stl` | RB9.01.060.010 | Main gripper frame | 1 | Houses servo and bearings |
| `clamp.stl` | RB9.01.060.020 | Gripper jaw/clamp | 2 | Contains LM6UU bearing seats |
| `gear-rack.stl` | RB9.01.060.030 | Linear gear rack | 2 | Converts rotation to linear motion |
| `drive-gear.stl` | RB9.01.060.040 | Drive gear | 1 | Mounts to servo output |

## 3D Printing Guidelines

### Recommended Settings
- **Layer Height**: 0.15-0.2mm
- **Infill**: 20% for frame/clamps, 30% for gears
- **Material**: PLA (prototyping), PETG (production)
- **Print Speed**: 50-60 mm/s
- **Nozzle Temperature**: 210°C (PLA), 240°C (PETG)
- **Bed Temperature**: 60°C (PLA), 80°C (PETG)

### Print Orientation
- **Main Frame**: Print upright for best surface finish
- **Clamps**: Print with bearing holes vertical
- **Gear Rack**: Print flat for best gear tooth quality
- **Drive Gear**: Print flat with gear teeth facing up

### Support Requirements
- **Main Frame**: Minimal supports may be needed
- **Clamps**: Supports required for bearing holes
- **Gear Rack**: No supports needed
- **Drive Gear**: No supports needed

### Post-Processing
1. **Remove supports** carefully to avoid damaging bearing seats
2. **Test fit bearings** - light sanding may be needed for proper fit
3. **Check gear mesh** - ensure smooth engagement between drive gear and racks
4. **Deburr all holes** for fasteners

## Material Considerations

### PLA (Recommended for Prototyping)
- ✅ Easy to print
- ✅ Good dimensional accuracy
- ✅ Low cost
- ❌ Limited temperature range
- ❌ Lower impact resistance

### PETG (Recommended for Production)
- ✅ Higher strength and flexibility
- ✅ Better temperature resistance
- ✅ Chemical resistance
- ❌ More challenging to print
- ❌ Higher cost

### ABS (Alternative)
- ✅ High strength
- ✅ Good temperature resistance
- ❌ Warping issues
- ❌ Requires heated enclosure

## Quality Control

### Dimensional Checks
- **Bearing fits**: LM6UU bearings should press-fit snugly
- **Rod clearance**: 6mm rods should slide smoothly
- **Gear mesh**: 0.2-0.3mm backlash between gears
- **Fastener holes**: M3/M4 screws should thread cleanly

### Functional Tests
1. **Bearing rotation**: All bearings should rotate freely
2. **Linear motion**: Clamps should slide smoothly on rods
3. **Gear engagement**: No binding or excessive noise
4. **Assembly fit**: All parts should assemble without force

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Bearings too tight | Over-extrusion | Scale holes +2%, sand lightly |
| Bearings too loose | Under-extrusion | Use thread locker or shims |
| Gear binding | Poor print quality | Reprint with finer layer height |
| Rod binding | Warped parts | Check printer calibration |

## File Information

- **Format**: STL (binary)
- **Units**: Millimeters
- **Coordinate System**: Standard (Z-up)
- **Created With**: Professional CAD software
- **Tested**: Multiple print iterations

---

**Print responsibly and ensure proper ventilation when 3D printing!** 🖨️ 