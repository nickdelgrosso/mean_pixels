# This is my project!
import statistics

def calculate_pixel_brightness(x, y, z):
    brightness = statistics.mean([x, y, z])
    return brightness

data = [1, 2, 3]
data_times_two = [x * 2 for x in data]  # [1, 4, 9]


pixel = {'red': 100, 'green': 0, 'blue': 0}
pixel2 = {'red': 50, 'green': 100, 'blue': 0}
pixels = [pixel, pixel2]

pixel_brightnesses = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]

pixel_brightness = calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue'])

pixel_brightness2 = calculate_pixel_brightness(pixel2['red'], pixel2['green'], pixel2['blue'])

mean_brightness = statistics.mean(pixel_brightnesses)
print(mean_brightness)
