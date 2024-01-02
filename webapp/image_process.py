import spectral
class image_process:
    def __init__(self) -> None:
        pass

    def spectral_to_rgb(self,image) -> list:
        img = spectral.open_image(image)
        r_band = img.read_band(red_band_index)
        g_band = img.read_band(green_band_index)
        b_band = img.read_band(blue_band_index)

        # Combine the channels to create the RGB image
        rgb_image = spectral.Image(img.width, img.height)
        rgb_image.bands = [r_band, g_band, b_band]
        return rgb_image.bands