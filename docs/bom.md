# Bill of Materials (BOM)

## Overview

This document lists all components required to build the parallel gripper. Links are provided to suggested suppliers, but equivalent parts from other vendors may be substituted.

## Electronic Components

| Item | Description | Qty | Supplier Link | Notes |
|------|-------------|-----|---------------|-------|
| ST-3215-C018 | Feetech Servo Motor STS3215 | 1 | [Feetech Official](https://www.feetechrc.com/525603.html) | High-precision bus servo with feedback |
| Bus Servo Adapter | Waveshare Bus Servo Adapter Board | 1 | [Waveshare](https://www.waveshare.com/bus-servo-adapter-a.htm) | TTL/RS485 communication interface |

## Mechanical Components

### Bearings

| Item | Description | Qty | Supplier Link | Notes |
|------|-------------|-----|---------------|-------|
| MR106ZZ | Ball Bearing 10×6×3 mm | 2 | [Amazon](https://www.amazon.com/ACROPIX-Bearings-Shielded-Pre-Lubricated-Deep-6x10x3mm/dp/B0C4PGLSCY/) | Shielded, pre-lubricated |
| LM6UU | Linear Bearing 12×6×19 mm | 4 | [Amazon](https://www.amazon.com/Skweawert-LM6UU-Linear-Bearings-Printer/dp/B0D5BGWCYB/) | For smooth linear motion |

### Rods

| Item | Description | Qty | Supplier Link | Notes |
|------|-------------|-----|---------------|-------|
| Steel Rod | Stainless Steel Rod 6mm × 150mm | 2 | [Amazon](https://www.amazon.com/150mm-Stainless-Industry-Working-Hobbies/dp/B0D5D2LB3Y/) | High precision, corrosion resistant |

## 3D-Printed Parts

| Part Number | Description | Qty | Material | Print Settings |
|-------------|-------------|-----|----------|----------------|
| RB9.01.060.010 | Main Frame | 1 | PLA/PETG | 0.2mm layer, 20% infill |
| RB9.01.060.020 | Clamp | 2 | PLA/PETG | 0.2mm layer, 20% infill |
| RB9.01.060.030 | Gear Rack | 2 | PLA/PETG | 0.15mm layer, 30% infill |
| RB9.01.060.040 | Drive Gear | 1 | PLA/PETG | 0.15mm layer, 30% infill |

### 3D Printing Notes
- **Material**: PLA recommended for prototyping, PETG for production use
- **Layer Height**: 0.15-0.2mm for optimal surface finish
- **Infill**: Higher infill (30%) recommended for gears to ensure strength
- **Support**: May be required depending on printer orientation
- **Post-processing**: Light sanding may be needed for bearing fits

## Fasteners

### Screws

| Item | Description | Qty | Standard | Notes |
|------|-------------|-----|----------|-------|
| M3×10 | Countersunk Screw | 4 | DIN 7991 | For gear rack attachment |
| M3×20 | Countersunk Screw | 4 | DIN 7991 | For clamp to rod attachment |
| M4×8 | Countersunk Screw | 2 | DIN 7991 | For main frame bearing retention |

### Nuts

| Item | Description | Qty | Standard | Notes |
|------|-------------|-----|----------|-------|
| M3 | Hex Nut | 4 | DIN 934 | For clamp assembly |

### Servo Hardware

| Item | Description | Qty | Source | Notes |
|------|-------------|-----|--------|-------|
| Self-tapping Screws | Servo mounting screws | 4 | Servo kit | Included with STS3215 |
| Servo Disk | Output shaft adapter | 1 | Servo kit | Included with STS3215 |
| Mounting Screw | Disk retention screw | 1 | Servo kit | Included with STS3215 |

## Cost Estimate

| Category | Estimated Cost (USD) |
|----------|---------------------|
| Electronic Components | $85-120 |
| Mechanical Components | $25-35 |
| 3D Printing Materials | $5-10 |
| Fasteners | $10-15 |
| **Total** | **$125-180** |

*Costs may vary based on supplier, quantity, and location*

## Sourcing Notes

### Alternative Suppliers
- **Bearings**: Local industrial suppliers often carry standard sizes
- **Rods**: Machine shops can cut custom lengths
- **Fasteners**: McMaster-Carr, Fastenal, or local hardware stores
- **Electronics**: Robotics specialty suppliers may offer better pricing

### Quality Considerations
- **Bearings**: Ensure proper ABEC rating for smooth operation
- **Rods**: Straightness tolerance critical for proper operation
- **Fasteners**: Stainless steel recommended for corrosion resistance

### Bulk Ordering
- Consider ordering extra fasteners for future builds
- 3D printing multiple sets reduces per-unit cost
- Group orders with robotics clubs/makerspaces for better pricing

## Compatibility Notes

### Servo Alternatives
The gripper is designed for the Feetech STS3215, but may be compatible with:
- Other Feetech STS series servos (with mounting modifications)
- Waveshare ST3215 (direct compatibility)
- Similar bus servos with 25T spline output

### Material Substitutions
- **Rods**: Carbon fiber or aluminum possible for weight reduction
- **Bearings**: Ceramic bearings for high-precision applications
- **3D Printing**: ABS, ASA, or Nylon for high-temperature environments

---

**Procurement Complete!** You should now have all components needed for assembly. 