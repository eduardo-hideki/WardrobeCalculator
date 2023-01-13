strucutural_thickness = 15#int(input("Insert structural material thickness: "))
backpanel_thickness = 6#int(input("Insert backpanel material thickness: "))

wardrobe_height = 2400#int(input("Insert desired wardrobe height (15 mm will be added): "))
wardrobe_width = 1700#int(input("Insert desired wardrobe width: "))
wardrobe_depth = 528#int(input("Insert desired wardrobe internal depth: "))
wardrobe_baseboard_height = 100#int(input("Insert wardrobe baseboard height: "))



class WardrobePiece(object):
    def __init__(self, name, quantitiy, height, width, thickness = 15):
        self.name = name
        self.height = height
        self.width = width
        self.thickness = thickness
        self.quantity = quantitiy

    def PrintDimensions(self):
        print("{} ({} pcs): {} mm x {} mm x {} mm".format(self.name, self.quantity, max(self.height, self.width), min(self.height, self.width), self.thickness))


wardrobe_external_depth = wardrobe_depth + 80 + 2 * backpanel_thickness

wardrobe_sides = WardrobePiece("Sides",
                               2,
                               wardrobe_height,
                               wardrobe_external_depth,
                               strucutural_thickness)
wardrobe_shelves = WardrobePiece("Shelves",
                                 4,
                                 (wardrobe_width - 3 * strucutural_thickness)/2,
                                 wardrobe_depth,
                                 strucutural_thickness)
wardrobe_divider = WardrobePiece("Divider",
                                 1,
                                 wardrobe_height - strucutural_thickness - wardrobe_baseboard_height,
                                 wardrobe_depth + 2 * backpanel_thickness)
wardrobe_floor = WardrobePiece("Floor",
                               1,
                               wardrobe_width - 2 * strucutural_thickness,
                               wardrobe_external_depth,
                               strucutural_thickness)
wardrobe_baseboard_long_beam = WardrobePiece("Baseboard long beam",
                                             2,
                                             wardrobe_width - 2 * strucutural_thickness,
                                             wardrobe_baseboard_height - strucutural_thickness,
                                             strucutural_thickness)
wardrobe_baseboard_short_beam = WardrobePiece("Baseboard short beam",
                                              3,
                                              wardrobe_external_depth - 2 * strucutural_thickness - 10,
                                              wardrobe_baseboard_height - strucutural_thickness,
                                              strucutural_thickness)
wardrobe_backpanels = WardrobePiece("Backpanel",
                                    2,
                                    wardrobe_height - wardrobe_baseboard_height + 2 * backpanel_thickness,
                                    (wardrobe_width - 3 * strucutural_thickness)/2 + 2 * backpanel_thickness,
                                    backpanel_thickness)

wardrobe = [wardrobe_sides,
            wardrobe_shelves,
            wardrobe_divider,
            wardrobe_floor,
            wardrobe_baseboard_long_beam,
            wardrobe_backpanels]
for wardrobe_part in wardrobe:
    wardrobe_part.PrintDimensions()
