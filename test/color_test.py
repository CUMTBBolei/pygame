#################################### IMPORTS ###################################

import unittest
import pygame

################################### CONSTANTS ##################################

rgba_vals = [0, 1, 62, 63, 126, 127, 255]

rgba_combinations =  [ (r,g,b,a) for r in rgba_vals
                                 for g in rgba_vals
                                 for b in rgba_vals
                                 for a in rgba_vals ]

################################################################################

# TODO: add tests for
# correct_gamma()
# hsva, hsla
# coerce ()

def _assignr (x, y):
    x.r = y

def _assigng (x, y):
    x.g = y

def _assignb (x, y):
    x.b = y

def _assigna (x, y):
    x.a = y

def _assign_item (x, p, y):
    x[p] = y

class ColorTest (unittest.TestCase):
    def test_color (self):
        c = pygame.Color (10, 20, 30, 40)
        self.assertEquals (c.r, 10)
        self.assertEquals (c.g, 20)
        self.assertEquals (c.b, 30)
        self.assertEquals (c.a, 40)

        c = pygame.Color ("indianred3")
        self.assertEquals (c.r, 205)
        self.assertEquals (c.g, 85)
        self.assertEquals (c.b, 85)
        self.assertEquals (c.a, 255)

        c = pygame.Color (0xAABBCCDD)
        self.assertEquals (c.r, 0xAA)
        self.assertEquals (c.g, 0xBB)
        self.assertEquals (c.b, 0xCC)
        self.assertEquals (c.a, 0xDD)

        self.assertRaises (ValueError, pygame.Color, 257, 10, 105, 44)
        self.assertRaises (ValueError, pygame.Color, 10, 257, 105, 44)
        self.assertRaises (ValueError, pygame.Color, 10, 105, 257, 44)
        self.assertRaises (ValueError, pygame.Color, 10, 105, 44, 257)

    def test_rgba (self):
        c = pygame.Color (0)
        self.assertEquals (c.r, 0)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 0)
        self.assertEquals (c.a, 0)

        # Test simple assignments
        c.r = 123
        self.assertEquals (c.r, 123)
        self.assertRaises (ValueError, _assignr, c, 537)
        self.assertEquals (c.r, 123)
        self.assertRaises (ValueError, _assignr, c, -3)
        self.assertEquals (c.r, 123)

        c.g = 55
        self.assertEquals (c.g, 55)
        self.assertRaises (ValueError, _assigng, c, 348)
        self.assertEquals (c.g, 55)
        self.assertRaises (ValueError, _assigng, c, -44)
        self.assertEquals (c.g, 55)

        c.b = 77
        self.assertEquals (c.b, 77)
        self.assertRaises (ValueError, _assignb, c, 256)
        self.assertEquals (c.b, 77)
        self.assertRaises (ValueError, _assignb, c, -12)
        self.assertEquals (c.b, 77)

        c.a = 255
        self.assertEquals (c.a, 255)
        self.assertRaises (ValueError, _assigna, c, 312)
        self.assertEquals (c.a, 255)
        self.assertRaises (ValueError, _assigna, c, -10)
        self.assertEquals (c.a, 255)
        
    def test_repr (self):
        c = pygame.Color (68, 38, 26, 69)
        t = "(68, 38, 26, 69)"
        self.assertEquals (repr (c), t)

    def test_add (self):
        c1 = pygame.Color (0)
        self.assertEquals (c1.r, 0)
        self.assertEquals (c1.g, 0)
        self.assertEquals (c1.b, 0)
        self.assertEquals (c1.a, 0)

        c2 = pygame.Color (20, 33, 82, 193)
        self.assertEquals (c2.r, 20)
        self.assertEquals (c2.g, 33)
        self.assertEquals (c2.b, 82)
        self.assertEquals (c2.a, 193)

        c3 = c1 + c2
        self.assertEquals (c3.r, 20)
        self.assertEquals (c3.g, 33)
        self.assertEquals (c3.b, 82)
        self.assertEquals (c3.a, 193)

        c3 = c3 + c2
        self.assertEquals (c3.r, 40)
        self.assertEquals (c3.g, 66)
        self.assertEquals (c3.b, 164)
        self.assertEquals (c3.a, 255)

    def test_sub (self):
        c1 = pygame.Color (0xFFFFFFFF)
        self.assertEquals (c1.r, 255)
        self.assertEquals (c1.g, 255)
        self.assertEquals (c1.b, 255)
        self.assertEquals (c1.a, 255)

        c2 = pygame.Color (20, 33, 82, 193)
        self.assertEquals (c2.r, 20)
        self.assertEquals (c2.g, 33)
        self.assertEquals (c2.b, 82)
        self.assertEquals (c2.a, 193)

        c3 = c1 - c2
        self.assertEquals (c3.r, 235)
        self.assertEquals (c3.g, 222)
        self.assertEquals (c3.b, 173)
        self.assertEquals (c3.a, 62)

        c3 = c3 - c2
        self.assertEquals (c3.r, 215)
        self.assertEquals (c3.g, 189)
        self.assertEquals (c3.b, 91)
        self.assertEquals (c3.a, 0)

    def test_mul (self):
        c1 = pygame.Color (0x01010101)
        self.assertEquals (c1.r, 1)
        self.assertEquals (c1.g, 1)
        self.assertEquals (c1.b, 1)
        self.assertEquals (c1.a, 1)

        c2 = pygame.Color (2, 5, 3, 22)
        self.assertEquals (c2.r, 2)
        self.assertEquals (c2.g, 5)
        self.assertEquals (c2.b, 3)
        self.assertEquals (c2.a, 22)

        c3 = c1 * c2
        self.assertEquals (c3.r, 2)
        self.assertEquals (c3.g, 5)
        self.assertEquals (c3.b, 3)
        self.assertEquals (c3.a, 22)

        c3 = c3 * c2
        self.assertEquals (c3.r, 4)
        self.assertEquals (c3.g, 25)
        self.assertEquals (c3.b, 9)
        self.assertEquals (c3.a, 255)

    def test_div (self):
        c1 = pygame.Color (0x80808080)
        self.assertEquals (c1.r, 128)
        self.assertEquals (c1.g, 128)
        self.assertEquals (c1.b, 128)
        self.assertEquals (c1.a, 128)

        c2 = pygame.Color (2, 4, 8, 16)
        self.assertEquals (c2.r, 2)
        self.assertEquals (c2.g, 4)
        self.assertEquals (c2.b, 8)
        self.assertEquals (c2.a, 16)

        c3 = c1 / c2
        self.assertEquals (c3.r, 64)
        self.assertEquals (c3.g, 32)
        self.assertEquals (c3.b, 16)
        self.assertEquals (c3.a, 8)

        c3 = c3 / c2
        self.assertEquals (c3.r, 32)
        self.assertEquals (c3.g, 8)
        self.assertEquals (c3.b, 2)
        self.assertEquals (c3.a, 0)

    def test_mod (self):
        c1 = pygame.Color (0xFFFFFFFF)
        self.assertEquals (c1.r, 255)
        self.assertEquals (c1.g, 255)
        self.assertEquals (c1.b, 255)
        self.assertEquals (c1.a, 255)

        c2 = pygame.Color (2, 4, 8, 16)
        self.assertEquals (c2.r, 2)
        self.assertEquals (c2.g, 4)
        self.assertEquals (c2.b, 8)
        self.assertEquals (c2.a, 16)

        c3 = c1 % c2
        self.assertEquals (c3.r, 1)
        self.assertEquals (c3.g, 3)
        self.assertEquals (c3.b, 7)
        self.assertEquals (c3.a, 15)

    def test_float (self):
        c = pygame.Color (0xCC00CC00)
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 0)
        self.assertEquals (float (c), float (0xCC00CC00))

        c = pygame.Color (0x33727592)
        self.assertEquals (c.r, 51)
        self.assertEquals (c.g, 114)
        self.assertEquals (c.b, 117)
        self.assertEquals (c.a, 146)
        self.assertEquals (float (c), float (0x33727592))

    def test_oct (self):
        c = pygame.Color (0xCC00CC00)
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 0)
        self.assertEquals (oct (c), oct (0xCC00CC00))

        c = pygame.Color (0x33727592)
        self.assertEquals (c.r, 51)
        self.assertEquals (c.g, 114)
        self.assertEquals (c.b, 117)
        self.assertEquals (c.a, 146)
        self.assertEquals (oct (c), oct (0x33727592))

    def test_hex (self):
        c = pygame.Color (0xCC00CC00)
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 0)
        self.assertEquals (hex (c), hex (0xCC00CC00))

        c = pygame.Color (0x33727592)
        self.assertEquals (c.r, 51)
        self.assertEquals (c.g, 114)
        self.assertEquals (c.b, 117)
        self.assertEquals (c.a, 146)
        self.assertEquals (hex (c), hex (0x33727592))


    def test_webstyle(self):
        c = pygame.Color ("#CC00CC11")
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 17)
        self.assertEquals (hex (c), hex (0xCC00CC11))

        c = pygame.Color ("#CC00CC")
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 0)
        self.assertEquals (hex (c), hex (0xCC00CC00))

        c = pygame.Color ("0xCC00CC11")
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 17)
        self.assertEquals (hex (c), hex (0xCC00CC11))

        c = pygame.Color ("0xCC00CC")
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 0)
        self.assertEquals (hex (c), hex (0xCC00CC00))

        self.assertRaises (ValueError, pygame.Color, "#cc00qq")
        self.assertRaises (ValueError, pygame.Color, "0xcc00qq")
        self.assertRaises (ValueError, pygame.Color, "09abcdef")
        self.assertRaises (ValueError, pygame.Color, "09abcde")
        self.assertRaises (ValueError, pygame.Color, "quarky")

    def test_int (self):
        # This will be a long
        c = pygame.Color (0xCC00CC00)
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 0)
        self.assertEquals (int (c), int (0xCC00CC00))

        # This will be an int
        c = pygame.Color (0x33727592)
        self.assertEquals (c.r, 51)
        self.assertEquals (c.g, 114)
        self.assertEquals (c.b, 117)
        self.assertEquals (c.a, 146)
        self.assertEquals (int (c), int (0x33727592))

    def test_long (self):
        # This will be a long
        c = pygame.Color (0xCC00CC00)
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 0)
        self.assertEquals (c.b, 204)
        self.assertEquals (c.a, 0)
        self.assertEquals (long (c), long (0xCC00CC00))

        # This will be an int
        c = pygame.Color (0x33727592)
        self.assertEquals (c.r, 51)
        self.assertEquals (c.g, 114)
        self.assertEquals (c.b, 117)
        self.assertEquals (c.a, 146)
        self.assertEquals (long (c), long (0x33727592))

    def test_normalize (self):
        c = pygame.Color (204, 38, 194, 55)
        self.assertEquals (c.r, 204)
        self.assertEquals (c.g, 38)
        self.assertEquals (c.b, 194)
        self.assertEquals (c.a, 55)

        t = c.normalize ()

        self.assertAlmostEquals (t[0], 0.800000, 5)
        self.assertAlmostEquals (t[1], 0.149016, 5)
        self.assertAlmostEquals (t[2], 0.760784, 5)
        self.assertAlmostEquals (t[3], 0.215686, 5)

    def test_len (self):
        c = pygame.Color (204, 38, 194, 55)
        self.assertEquals (len (c), 4)

    def test_get_item (self):
        c = pygame.Color (204, 38, 194, 55)
        self.assertEquals (c[0], 204)
        self.assertEquals (c[1], 38)
        self.assertEquals (c[2], 194)
        self.assertEquals (c[3], 55)

    def test_set_item (self):
        c = pygame.Color (204, 38, 194, 55)
        self.assertEquals (c[0], 204)
        self.assertEquals (c[1], 38)
        self.assertEquals (c[2], 194)
        self.assertEquals (c[3], 55)

        c[0] = 33
        self.assertEquals (c[0], 33)
        c[1] = 48
        self.assertEquals (c[1], 48)
        c[2] = 173
        self.assertEquals (c[2], 173)
        c[3] = 213
        self.assertEquals (c[3], 213)

        # Now try some 'invalid' ones
        self.assertRaises (ValueError, _assign_item, c, 0, 95.485)
        self.assertEquals (c[0], 33)
        self.assertRaises (ValueError, _assign_item, c, 1, -83)
        self.assertEquals (c[1], 48)
        self.assertRaises (ValueError, _assign_item, c, 2, "Hello")
        self.assertEquals (c[2], 173)

    def test_Color_type_works_for_Surface_set_colorkey(self):
        s = pygame.Surface((32, 32))
        for rgba in pygame.color.THECOLORS.itervalues():
            try:
                # this never seems to be caught :(
                # corrupt rest of tests ?
                s.set_colorkey(pygame.Color(*rgba))
                
            except OverflowError:
                self.assert_(False)

############### HSLA HSVA ALL ELEMENTS WITHIN SPECIFIED RANGE ##############

    def test_hsla__all_elements_within_limits(self):
        for (r, g, b, a) in rgba_combinations:
            c = pygame.Color (r,g,b,a)

            h, s, l, _a = c.hsla
            self.assert_(0 <= h <= 360)
            self.assert_(0 <= s <= 100)
            self.assert_(0 <= l <= 100)
            self.assert_(0 <= _a <= 100)

    def test_hsva__all_elements_within_limits(self):
        for (r, g, b, a) in rgba_combinations:
            c = pygame.Color (r,g,b,a)
        
            h, s, v, _a = c.hsva
            self.assert_(0 <= h <= 360)
            self.assert_(0 <= s <= 100)
            self.assert_(0 <= v <= 100)
            self.assert_(0 <= _a <= 100)

########### HSVA HSLA SANITY TESTS => CONVERTED SHOULD NOT RAISE ###########

    def test_hsla__sanity_testing_converted_should_not_raise(self):
        fails = 0        

        x = 0
        for r,g,b,a in rgba_combinations:
            x += 1
            
            c = pygame.Color (r,g,b,a)
            other = pygame.Color(0)

            try:
                other.hsla = c.hsla
                
            except ValueError:
                fails += 1
        
        self.assertEqual (
            (fails, x), (0, x)
        )

    def test_hsva__sanity_testing_converted_should_not_raise(self):
        fails = 0

        x = 0
        for r,g,b,a in rgba_combinations:
            x += 1 
            
            c = pygame.Color (r,g,b,a)
            other = pygame.Color(0)
            
            try:
                other.hsva = c.hsva
                
            except ValueError:
                fails += 1

        self.assertEqual (
            (fails, x), (0, x)
        )

    def test_hsla__sanity_testing_converted_should_equate(self):
        for r,g,b,a in rgba_combinations:            
            c = pygame.Color (r,g,b,a)
            other = pygame.Color(0)

            try:
                other.hsla = c.hsla

                self.assert_(abs(other.r - c.r) <= 1)
                self.assert_(abs(other.b - c.b) <= 1)
                self.assert_(abs(other.g - c.g) <= 1)
                self.assert_(abs(other.a - c.a) <= 1)
                
            except ValueError:
                pass                    # ??? other tests should catch
        
    def test_hsva__sanity_testing_converted_should_equate(self):
        for r,g,b,a in rgba_combinations:
            c = pygame.Color (r,g,b,a)
            other = pygame.Color(0)
            
            try:
                other.hsva = c.hsva
                
                self.assert_(abs(other.r - c.r) <= 1)
                self.assert_(abs(other.b - c.b) <= 1)
                self.assert_(abs(other.g - c.g) <= 1)
                self.assert_(abs(other.a - c.a) <= 1)
                
            except ValueError:
                pass
        
################################################################################

if __name__ == '__main__':    
    unittest.main()
