# This is my project!

RedValue = 100
RedValue2 = 50

GreenValue = 0
GreenValue2 = 100

BlueValue = 0
BlueValue2 = 0

ReadinessValue = 0
ReadinessValue2 = 200

pixel_brightness = (RedValue + GreenValue + BlueValue) / 3
pixel_brightness2 = (RedValue2 + GreenValue2 + BlueValue2) / 3

pixel_brightness3 = (pixel_brightness + pixel_brightness2) / 2
print(pixel_brightness3)
