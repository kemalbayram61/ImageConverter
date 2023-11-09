from Process.ImageConverter import ImageConverter
from Constants.ImageExtension import ImageExtension

if __name__ == '__main__':
    source_path = "C:\\Users\\Kemal Bayram\\Downloads"
    destination_path = "C:\\Users\\Kemal Bayram\\Downloads"
    max_read_per_period = 50
    image_converter = ImageConverter(source_path=source_path, destination_path=destination_path, max_read_per_period=max_read_per_period, source_extension=ImageExtension.HEIC)
    image_converter.start_converter()
