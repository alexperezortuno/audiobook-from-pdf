import platform
from os.path import dirname, abspath


class Utils:
    @staticmethod
    def read_content_file(path: str) -> str or None:
        file_data = open(path, "r")

        try:
            response = file_data.read()
            return response
        except Exception:
            return None
        finally:
            file_data.close()

    @staticmethod
    def platform_system(capitalize: bool = False) -> str:
        return str(platform.system()).capitalize() if capitalize else str(platform.system()).lower()

    def get_project_path(self) -> str:
        return self.parse_path(f'{dirname(dirname(abspath(__file__)))}')

    def parse_path(self, path: str) -> str:
        """
        Convert path by OS System
        :param: path: str
        :return: str
        """
        system_str: str = '{0}'.format(self.platform_system())
        if system_str == 'windows':
            return path.replace('/', '\\')
        elif system_str == 'linux':
            return path.replace('\\', '/')
        elif system_str == 'darwin':
            return path.replace('\\', '/')
