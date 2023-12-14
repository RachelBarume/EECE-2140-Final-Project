import unittest
from unittest.mock import patch, Mock
import pygame
import math

class TestGameFunctions(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_size_function(self):
        # Mock an image object for testing
        image_mock = Mock()
        image_mock.get_width.return_value = 100
        image_mock.get_height.return_value = 200

        # Test the size function
        resized_image = size(image_mock, 0.5)

        # Check if the size is halved
        self.assertEqual(resized_image.get_width(), 50)
        self.assertEqual(resized_image.get_height(), 100)

    def test_game_level_class(self):
        # Test GameLevel initialization
        game_level = GameLevel()
        self.assertEqual(game_level.level, 1)
        self.assertFalse(game_level.started)
        self.assertEqual(game_level.start_time, 0)

   
    def test_game_level_restart(self):
        # Test restarting the game
        game_level = GameLevel()
        game_level.level = 5
        game_level.started = True
        game_level.start_time = 12345
        game_level.restart()
        self.assertEqual(game_level.level, 1)
        self.assertFalse(game_level.started)
        self.assertEqual(game_level.start_time, 0)

    def test_game_level_exit_game(self):
        # Test exiting the game
        game_level = GameLevel()
        self.assertFalse(game_level.left_game())
        game_level.level = 2
        self.assertTrue(game_level.left_game())

    def test_general_car_class(self):
        # Test GeneralCar initialization
        general_car = GeneralCar(10, 20, 30)
        self.assertEqual(general_car.car_speed, 10)
        self.assertEqual(general_car.rotation_speed, 20)
        self.assertEqual(general_car.rotation_angle, 30)

    def test_general_car_move_forward(self):
        # Test moving forward for GeneralCar
        general_car = GeneralCar(10, 20, 30)
        new_x, new_y = general_car.move_forward(100, 200)
        # Adjusted position should be (100 - 10*sin(30), 200 - 10*cos(30))
        self.assertAlmostEqual(new_x, 94.57, places=2)
        self.assertAlmostEqual(new_y, 194.98, places=2)

    def test_general_car_move_backward(self):
        # Test moving backward for GeneralCar
        general_car = GeneralCar(10, 20, 30)
        new_x, new_y = general_car.move_backward(100, 200)
        # Adjusted position should be (100 + 10*sin(30), 200 + 10*cos(30))
        self.assertAlmostEqual(new_x, 105.42, places=2)
        self.assertAlmostEqual(new_y, 205.01, places=2)

    def test_general_car_adjust_position(self):
        # Test adjusting position for GeneralCar
        general_car = GeneralCar(10, 20, 30)
        adjusted_position = general_car.adjust_position(300, 400)
        # Adjusted position should be (WIDTH, HEIGHT) as defined in the code
        self.assertEqual(adjusted_position, (WIDTH, HEIGHT))

    def test_player_class(self):
        # Test Player initialization
        player = Player(100, 200, 30, 10, 20)
        self.assertEqual(player.x, 100)
        self.assertEqual(player.y, 200)
        self.assertEqual(player.rotation_angle, 30)
        self.assertEqual(player.car_speed, 10)
        self.assertEqual(player.rotation_speed, 20)

    @patch('pygame.key.get_pressed', return_value={pygame.K_RIGHT: True, pygame.K_LEFT: False, pygame.K_UP: True, pygame.K_DOWN: False})
    def test_player_keyboard_control(self, mock_key_pressed):
        # Test Player keyboard control
        player = Player(100, 200, 30, 10, 20)
        player.keyboard_control()
        # After pressing right and up, the rotation_angle should decrease and move_forward should be called
        self.assertEqual(player.rotation_angle, 10)
        # Ensure that the move_forward method is called
        player.move_forward.assert_called_once_with(100, 200)

if __name__ == '__main__':
    unittest.main()
