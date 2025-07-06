# Bill of Materials (BOM) / Amazon

## Overview

This document lists all components required to build the parallel gripper. Links are provided to suggested suppliers, but equivalent parts from other vendors may be substituted.

## Electronic Components

| Item | Description | Qty | Supplier Link | Price |  Notes |
|------|-------------|-----|---------------|-------|--------|
| ST3215 Servo | Waveshare Servo Motor STS3215 | 1 | [Amazon – Feetech STS3215 Servo](https://www.amazon.com/Precision-Programmable-Magnetic-Switchable-XYGStudy/dp/B0B95TFJ4H) | $28.99 | High-precision bus servo with feedback |
| Bus Servo Adapter | Waveshare Bus Servo Adapter Board | 1 | [Amazon – Bus Servo Adapter A](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP) | $10.99 | TTL/RS485 communication interface |

## Mechanical Components

### Bearings

| Item | Description | Qty | Supplier Link | Price | Notes |
|------|-------------|-----|---------------|-------|-------|
| MR106ZZ | Ball Bearing 10×6×3 mm | 2 | [Amazon – ACROPIX MR106ZZ Bearings (10pcs)](https://www.amazon.com/ACROPIX-Bearings-Shielded-Pre-Lubricated-Deep-6x10x3mm/dp/B0C4PGLSCY) | $5.49 (10pcs) | Shielded, pre-lubricated |
| LM6UU | Linear Bearing 6×12×19 mm | 4 | [Amazon – uxcell LM6UU Bearings (4pcs)](https://www.amazon.com/uxcell-LM6UU-Linear-Bearings-Length/dp/B07H95CWTX) | $8.99 (4pcs) | For smooth linear motion |

### Rods

| Item | Description | Qty | Supplier Link | Price | Notes |
|------|-------------|-----|---------------|-------|-------|
| Steel Rod | Stainless Steel Rod 6mm × 150mm | 2 | [Amazon – uxcell Stainless Steel Rod 6mm×150mm (5pcs)](https://www.amazon.com/uxcell-150mm-Stainless-Steel-Solid/dp/B082ZP51W8) | $8.39 (5pcs) | High precision, corrosion resistant |

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

| Item | Description | Qty | Standard | Price | Notes |
|------|-------------|-----|----------|-------|-------|
| M3×10 | Countersunk Screw | 4 | [Amazon – M3×10 Countersunk Screws](https://www.amazon.com/dp/B07JW9XF4Z) | $6.39 (100pcs) | For gear rack attachment |
| M3×20 | Countersunk Screw | 4 | [Amazon – M3×20 Countersunk Screws](https://www.amazon.com/dp/B0C6Z6DJ7V) | $6.99 (100pcs) | For clamp to rod attachment |
| M4×8 | Countersunk Screw | 2 | [Amazon – M4×8 Countersunk Screws](https://www.amazon.com/dp/B07JHD5YMV) | $9.99 (100pcs) | For main frame bearing retention |

### Nuts

| Item | Description | Qty | Standard | Price | Notes |
|------|-------------|-----|----------|-------|-------|
| M3 | Hex Nut | 4 | [Amazon – M3 Hex Nuts](https://www.amazon.com/dp/B07T7NCS7D) | $5.99 (100pcs) | For clamp assembly |

### Servo Hardware

| Item | Description | Qty | Source | Price | Notes |
|------|-------------|-----|--------|-------|-------|
| Self-tapping Screws | Servo mounting screws | 4 | Servo kit | Included | Included with STS3215 |
| Servo Disk | Output shaft adapter | 1 | Servo kit | Included | Included with STS3215 |
| Mounting Screw | Disk retention screw | 1 | Servo kit | Included | Included with STS3215 |

## Cost Estimate

| Category | Estimated Cost (USD) |
|----------|---------------------|
| Electronic Components | $39.98 |
| Mechanical Components | $22.87 |
| 3D Printing Materials | $5-10 |
| Fasteners | $1.60 (approximate) |
| **Total** | **$69.45-74.45** |

*Costs based on Amazon pricing as of current date. Bulk quantities provide significant savings on fasteners.*

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