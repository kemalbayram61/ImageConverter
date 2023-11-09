import math

from PIL import Image

from Constants.ImageExtension import ImageExtension
from Process.ImageLoader import ImageLoader


class ImageConverter:
    __source_path: str
    __destination_path: str
    __source_extension: ImageExtension
    __destination_extension: ImageExtension
    __max_read_by_period: int
    __image_loader: ImageLoader

    def __init__(self, **context):
        self.__source_path = context['source_path']
        self.__destination_path = context['destination_path']
        self.__max_read_by_period = context["max_read_per_period"]

        if 'source_extension' in context.keys():
            self.__source_extension = context['source_extension']
        else:
            self.__source_extension = ImageExtension.HEIF

        if 'destination_extension' in context.keys():
            self.__destination_extension = context['destination_extension']
        else:
            self.__destination_extension = ImageExtension.JPG

        self.__image_loader = ImageLoader(source_path=self.__source_path, image_extension=self.__source_extension,
                                          max_read_per_period=self.__max_read_by_period)

    def convert_image_list(self, image_list: list[Image], file_name_list: list[str]):
        for index, image in enumerate(image_list):
            file_name = file_name_list[index]
            print("{0} isimli dosya donusturuluyor.".format(file_name))
            file_name = file_name[:file_name.rindex(".")]
            image.convert("RGB").save("{0}\\{1}{2}".format(self.__destination_path, file_name, self.__destination_extension.value))
            print("{0} isimli dosya donusturuldu.".format(file_name))

    def start_converter(self):
        source_image_count = self.__image_loader.get_source_image_count()
        convert_step_count = math.ceil(source_image_count / self.__max_read_by_period)

        for part_index in range(convert_step_count):
            image_list_part: list[Image] = self.__image_loader.get_image_list(part_index)
            file_name_list: list[str] = self.__image_loader.get_source_image_name_list_part(part_index)
            self.convert_image_list(image_list_part, file_name_list)
