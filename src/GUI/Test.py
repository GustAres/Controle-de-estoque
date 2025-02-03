import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QSizePolicy
from PySide6.QtGui import QPalette, QColor, QPainter, QPainterPath, QPixmap, QIcon
from PySide6.QtCore import Qt, QRect, QSize

# Definindo constantes
BACKGROUND_COLOR = QColor(127, 0, 255)
BUTTON_COLOR = QColor(0, 0, 0)
BUTTON_TEXT_COLOR = QColor(255, 255, 255)
BUTTON_PRESSED_COLOR = QColor(68, 68, 68)
WINDOW_COLOR = QColor(0, 0, 0)
IMAGE_PATH = r"C:\Users\conta\PycharmProjects\GUI\Images\IconP.png"
BACK_ICON_PATH = r"C:\Users\conta\PycharmProjects\GUI\Images\seta.png"

class RoundedRectangleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = "Bem vindo ao Estoque GT"
        self.setStyleSheet(
            f"background-color: rgb({BACKGROUND_COLOR.red()}, {BACKGROUND_COLOR.green()}, {BACKGROUND_COLOR.blue()}); border-radius: 20px;")

        # Layout para os botões e o texto dentro do retângulo
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(20)

        # Título centralizado no topo
        self.title_label = QLabel(self.title, self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title_label)

        # Botões serão adicionados a este layout
        self.button_layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)

    def paintEvent(self, event):
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        path.addRoundedRect(rect, 20, 20)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)
        painter.setBrush(BACKGROUND_COLOR)
        painter.setPen(Qt.NoPen)
        painter.drawRect(rect)

class ProductRegistrationScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Cadastro de Produto')
        self.setStyleSheet(
            f"background-color: rgb({WINDOW_COLOR.red()}, {WINDOW_COLOR.green()}, {WINDOW_COLOR.blue()});")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Adiciona o botão de voltar no canto superior esquerdo
        back_button = self.create_back_button()
        layout.addWidget(back_button, alignment=Qt.AlignTop | Qt.AlignLeft)

        self.setLayout(layout)

    def create_back_button(self):
        button = QPushButton(self)
        button.setIcon(QIcon(BACK_ICON_PATH))
        button.setIconSize(QSize(24, 24))
        button.setFixedSize(50, 50)  # Define o tamanho fixo do botão para ser circular
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: rgb({BUTTON_COLOR.red()}, {BUTTON_COLOR.green()}, {BUTTON_COLOR.blue()});
                border: 2px solid rgb({BACKGROUND_COLOR.red()}, {BACKGROUND_COLOR.green()}, {BACKGROUND_COLOR.blue()});
                border-radius: 25px;
                padding: 10px;
            }}
            QPushButton:pressed {{
                background-color: rgb({BUTTON_PRESSED_COLOR.red()}, {BUTTON_PRESSED_COLOR.green()}, {BUTTON_PRESSED_COLOR.blue()});
            }}
        """)
        button.clicked.connect(self.parent().show_main_screen)
        return button

class AddProductScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Adicionar Produto')
        self.setStyleSheet(
            f"background-color: rgb({WINDOW_COLOR.red()}, {WINDOW_COLOR.green()}, {WINDOW_COLOR.blue()});")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Adiciona o botão de voltar no canto superior esquerdo
        back_button = self.create_back_button()
        layout.addWidget(back_button, alignment=Qt.AlignTop | Qt.AlignLeft)

        self.setLayout(layout)

    def create_back_button(self):
        button = QPushButton(self)
        button.setIcon(QIcon(BACK_ICON_PATH))
        button.setIconSize(QSize(24, 24))
        button.setFixedSize(50, 50)  # Define o tamanho fixo do botão para ser circular
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: rgb({BUTTON_COLOR.red()}, {BUTTON_COLOR.green()}, {BUTTON_COLOR.blue()});
                border: 2px solid rgb({BACKGROUND_COLOR.red()}, {BACKGROUND_COLOR.green()}, {BACKGROUND_COLOR.blue()});
                border-radius: 25px;
                padding: 10px;
            }}
            QPushButton:pressed {{
                background-color: rgb({BUTTON_PRESSED_COLOR.red()}, {BUTTON_PRESSED_COLOR.green()}, {BUTTON_PRESSED_COLOR.blue()});
            }}
        """)
        button.clicked.connect(self.parent().show_main_screen)
        return button

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Cria o retângulo com bordas arredondadas
        self.rounded_rect = RoundedRectangleWidget(self)
        self.rounded_rect.setFixedWidth(270)  # Define largura fixa para o retângulo arredondado

        # Adiciona o retângulo ao layout principal
        self.main_layout.addWidget(self.rounded_rect)

        # Adiciona a imagem centralizada
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(True)
        pixmap = QPixmap(IMAGE_PATH)

        # Sobrepor a cor da imagem
        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(Qt.transparent)

        painter = QPainter(colored_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(colored_pixmap.rect(), BACKGROUND_COLOR)
        painter.end()

        self.image_label.setPixmap(colored_pixmap)

        # Define a política de tamanho para a imagem
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Use Fixed para evitar expansão
        self.image_label.setMinimumSize(300, 300)

        # Adiciona a imagem ao layout principal sem expandi-la
        self.main_layout.addWidget(self.image_label, 0)

        # Adiciona os botões dentro do retângulo com bordas arredondadas
        self.add_button_to_layout(self.rounded_rect.button_layout, "Cadastrar Produto",
                                  self.show_product_registration_screen)
        self.add_button_to_layout(self.rounded_rect.button_layout, "Adicionar Produto", self.show_add_product_screen)

        # Cria o layout principal e adiciona o layout do retângulo
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)

        # Botão alterna entre as janelas
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(main_widget)
        self.product_registration_screen = ProductRegistrationScreen(self)
        self.stacked_widget.addWidget(self.product_registration_screen)
        self.add_product_screen = AddProductScreen(self)
        self.stacked_widget.addWidget(self.add_product_screen)

        # Define o layout principal como o stacked widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        # Define o título e o tamanho da janela principal
        self.setWindowTitle('Estoque GT')
        self.resize(950, 500)
        self.setMinimumSize(950, 500)

        # Define a cor de fundo da janela
        palette = QPalette()
        palette.setColor(QPalette.Window, WINDOW_COLOR)
        self.setPalette(palette)

    def showEvent(self, event):
        super().showEvent(event)
        # Ajusta o tamanho e a posição dos widgets quando a janela é mostrada
        self.adjustSize()
        self.update_geometry()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_geometry()

    def update_geometry(self):
        # Ajusta o tamanho do retângulo para cobrir a altura da janela
        self.rounded_rect.setGeometry(7, 7, 270, self.height() - 40)

        # Ajusta a imagem para centralizar e redimensionar conforme a janela
        image_width = int((self.width() - 310) * 0.6)  # 60% da largura disponível
        image_height = int(self.height() * 0.6)  # 60% da altura da janela
        image_x = 310 + (self.width() - 310 - image_width) // 2
        image_y = (self.height() - image_height) // 2
        self.image_label.setGeometry(image_x, image_y, image_width, image_height)

    def add_button_to_layout(self, layout, text, callback):
        button = QPushButton(text, self.rounded_rect)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: rgb({BUTTON_COLOR.red()}, {BUTTON_COLOR.green()}, {BUTTON_COLOR.blue()});
                color: rgb({BUTTON_TEXT_COLOR.red()}, {BUTTON_TEXT_COLOR.green()}, {BUTTON_TEXT_COLOR.blue()});
                border-radius: 15px;
                padding: 10px 20px;
            }}
            QPushButton:pressed {{
                background-color: rgb({BUTTON_PRESSED_COLOR.red()}, {BUTTON_PRESSED_COLOR.green()}, {BUTTON_PRESSED_COLOR.blue()});
            }}
        """)
        button.clicked.connect(callback)
        layout.addWidget(button)

    def show_product_registration_screen(self):
        self.stacked_widget.setCurrentWidget(self.product_registration_screen)

    def show_add_product_screen(self):
        self.stacked_widget.setCurrentWidget(self.add_product_screen)

    def show_main_screen(self):
        self.stacked_widget.setCurrentIndex(0)

def main():
    app = QApplication(sys.argv)

    # Cria a janela principal
    window = MainWindow()

    # Exibe a janela principal
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()