#!/usr/bin/env python3
"""
Basic Usage Example - Parallel Gripper
======================================

This example demonstrates basic gripper operations:
- Opening and closing the gripper
- Moving to specific positions
- Reading status information

Make sure to adjust the configuration parameters (port, servo ID) 
before running this example.
"""

import sys
import os
import time

# Add the software/python directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'software', 'python'))

from gripper_control import ParallelGripper, GripperConfig

def main():
    """Basic gripper usage example"""
    print("🤖 Basic Gripper Usage Example")
    print("=" * 40)
    
    # Create custom configuration if needed
    config = GripperConfig()
    # config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
    # config.STS_ID = 1                   # Servo ID
    
    # Create gripper instance
    gripper = ParallelGripper(config)
    
    try:
        # Connect to gripper
        print("📡 Connecting to gripper...")
        if not gripper.connect():
            print("❌ Failed to connect!")
            return 1
        
        print("✅ Connected successfully!")
        
        # Get initial status
        print("\n📊 Initial Status:")
        status = gripper.get_status()
        if status:
            print(f"  Position: {status['degrees']:.1f}°")
            print(f"  Temperature: {status['temperature']}°C")
            print(f"  Voltage: {status['voltage']:.1f}V")
        
        # Example movements
        movements = [
            ("Opening gripper", 45),
            ("Closing gripper", -45),
            ("Center position", 0),
            ("Wide open", 90),
            ("Fully closed", -90),
        ]
        
        for description, angle in movements:
            print(f"\n🔄 {description} (moving to {angle}°)...")
            
            if gripper.move_to_angle(angle):
                target_pos = gripper.degrees_to_position(angle)
                gripper.wait_for_completion(target_pos, timeout=5.0)
                
                # Show final status
                status = gripper.get_status()
                if status:
                    print(f"  Final position: {status['degrees']:.1f}°")
                    print(f"  Load: {status['load_percent']}%")
            else:
                print("  ❌ Movement failed!")
            
            time.sleep(1)  # Brief pause between movements
        
        print("\n✅ Example completed successfully!")
        
    except KeyboardInterrupt:
        print("\n⏹️ Example interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1
    finally:
        gripper.disconnect()
        print("👋 Disconnected from gripper")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 