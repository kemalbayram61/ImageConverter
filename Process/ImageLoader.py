from PIL import Image
from pillow_heif import register_heif_opener
import os

from Constants.ImageExtension import ImageExtension


class ImageLoader:
    __source_image_extension: ImageExtension
    __source_images_path: str
    __max_read_by_period: int

    def __init__(self, **context):
        self.__source_images_path = context["source_path"]
        self.__max_read_by_period = context["max_read_per_period"]
        if "image_extension" in context.keys():
            self.__source_image_extension = context["image_extension"]
        else:
            self.__source_image_extension = ImageExtension.HEIF

    def get_source_image_name_list(self) -> list[str]:
        all_elements = os.listdir(self.__source_images_path)
        response: list[str] = []
        for element in all_elements:
            if element.endswith(self.__source_image_extension.value):
                response.append(element)
        return response

    def get_source_image_count(self) -> int:
        all_elements = os.listdir(self.__source_images_path)
        response: list[str] = []
        for element in all_elements:
            if element.endswith(self.__source_image_extension.value):
                response.append(element)
        return len(response)

    def get_source_image_name_list_part(self, index) -> list[str]:
        all_elements = os.listdir(self.__source_images_path)
        response: list[str] = []
        for element in all_elements:
            if element.endswith(self.__source_image_extension.value):
                response.append(element)
        response = response[index * self.__max_read_by_period: (index + 1) * self.__max_read_by_period - 1]
        return response

    def get_image_list(self, index) -> list[Image]:
        register_heif_opener()
        response: list[Image] = []
        image_name_list = self.get_source_image_name_list_part(index)
        for image_name in image_name_list:
            response.append(Image.open("{0}\\{1}".format(self.__source_images_path, image_name)))
        return response

