"""
Auteur : Acori Ross
Date : 2025-04-25
Titre : Dessin d'une ferme avec la librairie Arcade.
"""

import arcade
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color((135, 206, 235, 255))

    def setup(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()

        # =====================
        # soleil
        # =====================
        sun_x, sun_y = 680, 530
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x1 = sun_x + math.cos(rad) * 38
            y1 = sun_y + math.sin(rad) * 38
            x2 = sun_x + math.cos(rad) * 55
            y2 = sun_y + math.sin(rad) * 55
            arcade.draw_line(x1, y1, x2, y2, arcade.color.YELLOW, 3)
        arcade.draw_circle_filled(sun_x, sun_y, 35, (255, 220, 50))

        # =====================
        # nuages
        # =====================
        def draw_cloud(cx, cy, scale=1.0):
            color = (255, 255, 255)
            arcade.draw_ellipse_filled(cx, cy, int(90 * scale), int(40 * scale), color)
            arcade.draw_ellipse_filled(cx - int(30 * scale), cy + int(10 * scale), int(55 * scale), int(35 * scale), color)
            arcade.draw_ellipse_filled(cx, cy + int(20 * scale), int(50 * scale), int(38 * scale), color)

        draw_cloud(150, 520, 1.2)



        # =====================
        # sol
        # =====================
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, 280, (34, 139, 34))

        # zone de terre brune (champ labouré sous le tracteur)
        arcade.draw_lrbt_rectangle_filled(400, SCREEN_WIDTH, 0, 200, (101, 67, 33))

        # délimite
        arcade.draw_line(400, 0, 400, 200, (60, 40, 15), 3)



        # =====================
        # chemin en terre
        # =====================
        arcade.draw_triangle_filled(170, 0, 230, 0, 200, 175, (139, 115, 85))

        # =====================
        # arbre (loin de guache)
        # =====================
        def draw_tree(x, y, trunk_h=80, crown_r=45, color_trunk=arcade.color.BROWN, color_crown=(20, 100, 20)):
            """
            Dessine un arbre à la position (x, y).
            trunk_h : hauteur du tronc
            crown_r : rayon du feuillage
            """
            arcade.draw_lrbt_rectangle_filled(x - 8, x + 8, y, y + trunk_h, color_trunk)
            arcade.draw_circle_filled(x, y + trunk_h + crown_r - 10, crown_r, color_crown)
            arcade.draw_circle_filled(x - 15, y + trunk_h + crown_r - 25, int(crown_r * 0.8), color_crown)
            arcade.draw_circle_filled(x + 15, y + trunk_h + crown_r - 25, int(crown_r * 0.8), color_crown)
            arcade.draw_circle_filled(x, y + trunk_h + crown_r + 5, int(crown_r * 0.75), (20, 100, 20))

        draw_tree(30, 220, 70, 40, (100, 60, 20), (20, 100, 20))
        draw_tree(75, 215, 75, 42, (100, 60, 20), (20, 100, 20))
        draw_tree(120, 218, 68, 38, (100, 60, 20), (20, 100, 20))
        draw_tree(680, 210, 65, 38, (100, 60, 20), (20, 100, 20))
        draw_tree(730, 205, 72, 40, (100, 60, 20), (20, 100, 20))
        # =====================
        # house
        # =====================
        hx, hy = 130, 175

        # foundation de la maison
        arcade.draw_lrbt_rectangle_filled(hx - 5, hx + 185, hy - 10, hy + 5, (150, 140, 130))

        # murs de la maison
        arcade.draw_lrbt_rectangle_filled(hx, hx + 180, hy, hy + 130, (245, 230, 200))

        # le toit principal
        arcade.draw_triangle_filled(
            hx - 20, hy + 130,
            hx + 200, hy + 130,
            hx + 90, hy + 220,
            (160, 50, 30)
        )
        # le bord du toit
        arcade.draw_lrbt_rectangle_filled(hx - 22, hx + 202, hy + 127, hy + 135, (120, 35, 15))

        # la cheminee
        arcade.draw_lrbt_rectangle_filled(hx + 130, hx + 158, hy + 155, hy + 215, (150, 100, 80))
        arcade.draw_lrbt_rectangle_filled(hx + 126, hx + 162, hy + 210, hy + 220, (130, 85, 65))

        # fumee de cheminée
        arcade.draw_circle_filled(hx + 144, hy + 230, 6,  (200, 200, 200))
        arcade.draw_circle_filled(hx + 147, hy + 248, 9,  (200, 200, 200))
        arcade.draw_circle_filled(hx + 142, hy + 266, 12, (200, 200, 200))


        # porte
        arcade.draw_lrbt_rectangle_filled(hx + 70, hx + 110, hy, hy + 75, (101, 67, 33))
        arcade.draw_ellipse_filled(hx + 90, hy + 75, 40, 20, (101, 67, 33))
        arcade.draw_lrbt_rectangle_outline(hx + 73, hx + 107, hy + 3, hy + 72, (80, 50, 20), 2)
        arcade.draw_circle_filled(hx + 106, hy + 38, 4, (200, 165, 50))
        arcade.draw_lrbt_rectangle_filled(hx + 62, hx + 118, hy - 10, hy + 3, (180, 160, 140))

        # fenetre gauche
        arcade.draw_lrbt_rectangle_filled(hx + 10, hx + 58, hy + 50, hy + 100, (173, 216, 230))

        # fenetre droite
        arcade.draw_lrbt_rectangle_filled(hx + 122, hx + 170, hy + 50, hy + 100, (173, 216, 230))

        # fenetre haut
        arcade.draw_triangle_filled(hx + 72, hy + 148, hx + 108, hy + 148, hx + 90, hy + 178, (173, 216, 230))

        # =====================
        # TRACTEUR
        # =====================
        tx, ty = 500, 50

        # roue arrière (la grande)
        arcade.draw_circle_filled(tx + 45, ty + 45, 45, (30, 30, 30))
        arcade.draw_circle_filled(tx + 45, ty + 45, 38, (50, 50, 50))
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            arcade.draw_line(
                tx + 45, ty + 45,
                tx + 45 + math.cos(rad) * 30, ty + 45 + math.sin(rad) * 30,
                (80, 80, 80),
            )



        # roue avant (la petite)
        arcade.draw_circle_filled(tx + 130, ty + 30, 30, (30, 30, 30))
        arcade.draw_circle_filled(tx + 130, ty + 30, 24, (50, 50, 50))
        for angle in range(0, 360, 60):
            rad = math.radians(angle)
            arcade.draw_line(
                tx + 130, ty + 30,
                tx + 130 + math.cos(rad) * 18, ty + 30 + math.sin(rad) * 18,
                (80, 80, 80), 2
            )

        # chassis
        arcade.draw_lrbt_rectangle_filled(tx + 30, tx + 150, ty + 45, ty + 95, (200, 35, 25))
        arcade.draw_lrbt_rectangle_filled(tx + 30, tx + 150, ty + 88, ty + 95, (200, 35, 25))

        # capot moteur
        arcade.draw_lrbt_rectangle_filled(tx + 95, tx + 160, ty + 60, ty + 95, (200, 35, 25))
        arcade.draw_ellipse_filled(tx + 160, ty + 77, 20, 35, (200, 35, 25))

        # pot d'echappement en gaz
        arcade.draw_lrbt_rectangle_filled(tx + 152, tx + 160, ty + 95, ty + 120, (80, 80, 80))

        # la cabine
        arcade.draw_lrbt_rectangle_filled(tx + 30, tx + 100, ty + 95, ty + 145, (180, 30, 20))
        arcade.draw_lrbt_rectangle_filled(tx + 25, tx + 105, ty + 142, ty + 150, (180, 30, 20))

        # pare brise
        arcade.draw_lrbt_rectangle_filled(tx + 75, tx + 97, ty + 100, ty + 140, (173, 216, 230))

        # fenetre
        arcade.draw_lrbt_rectangle_filled(tx + 33, tx + 60, ty + 108, ty + 138, (173, 216, 230))

        # siege et volant


        # marche pied
        arcade.draw_lrbt_rectangle_filled(tx + 28, tx + 50, ty + 55, ty + 62, (150, 20, 10))

        # bras hydraulique
        arcade.draw_lrbt_rectangle_filled(tx - 20, tx + 32, ty + 55, ty + 65, (200, 35, 25))
        arcade.draw_lrbt_rectangle_filled(tx - 30, tx - 18, ty + 30, ty + 65, (180, 30, 20))
        for i in range(5):
            arcade.draw_triangle_filled(
                tx - 30 - i * 8, ty + 30,
                tx - 22 - i * 8, ty + 30,
                tx - 26 - i * 8, ty + 10,
                (150, 150, 150)
            )

        # phar avant
        arcade.draw_circle_filled(tx + 162, ty + 85, 7, (255, 255, 200))
        arcade.draw_circle_outline(tx + 162, ty + 85, 7, (150, 20, 10), 2)

        # =====================
        # decoration
        # =====================



        # affiche
        arcade.draw_lrbt_rectangle_filled(453, 459, 130, 200, (110, 70, 30))
        arcade.draw_lrbt_rectangle_filled(445, 480, 195, 215, (130, 85, 40))
        arcade.draw_text("FERME", 446, 197, arcade.color.WHITE, 8)

        # titre
        arcade.draw_text("ma belle ferme", 260, 570, (255, 255, 255), 26,
                         bold=True, font_name="Arial")


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "la belle ferme")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

