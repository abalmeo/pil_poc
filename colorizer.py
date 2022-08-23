from re import A
from PIL import Image, ImageDraw


colors = [
    {'name': 'Apricot', 'hex_code': '#EEC1AA'},
    {'name': 'Black', 'hex_code': '#1B181B'},
    {'name': 'Blue', 'hex_code': '#51517B'},
    {'name': 'Blush', 'hex_code': '#DDBBBF'},
    {'name': 'Brown', 'hex_code': '#815D4D'},
    {'name': 'Brass', 'hex_code': '#343130'},
    {'name': 'Burgundy', 'hex_code': '#871D27'},
    {'name': 'Butter', 'hex_code': '#D0B376'},
    {'name': 'Cadet Blue', 'hex_code': '#4579A7'},
    {'name': 'Champagne', 'hex_code': '#DCCDB7'},
    {'name': 'Charcoal', 'hex_code': '#54535B'},
    {'name': 'Chianti', 'hex_code': '#733947'},
    {'name': 'Cinnamon', 'hex_code': '#67231F'},
    {'name': 'Cobalt Blue', 'hex_code': '#4470AA'},
    {'name': 'Coral', 'hex_code': '#EB6D6D'},
    {'name': 'Daffodil', 'hex_code': '#F2CD92'},
    {'name': 'Deep Peach', 'hex_code': '#F6C1B6'},
    {'name': 'Deep Purple', 'hex_code': '#606082'},
    {'name': 'Deep Rose', 'hex_code': '#8B2E57'},
    {'name': 'Deep Teal', 'hex_code': '#125B7D'},
    {'name': 'Dusty Blue', 'hex_code': '#88A2C3'},
    {'name': 'Eggplant', 'hex_code': '#532D4F'},
    {'name': 'Emerald', 'hex_code': '#3D5C66'},
    {'name': 'Eucalyptus', 'hex_code': '#8A8775'},
    {'name': 'Gold', 'hex_code': '#F4D27B'},
    {'name': 'Grape', 'hex_code': '#34263D'},
    {'name': 'Gray Cotton', 'hex_code': '#64616B'},
    {'name': 'Green', 'hex_code': '#2E5948'},
    {'name': 'Grey', 'hex_code': '#65626A'},
    {'name': 'Juniper', 'hex_code': '#243930'},
    {'name': 'Khaki', 'hex_code': '#CEBCA4'},
    {'name': 'Lavender', 'hex_code': '#C7B3D1'},
    {'name': 'Light Grey', 'hex_code': '#BAC2CB'},
    {'name': 'Lilac', 'hex_code': '#C4B7CC'},
    {'name': 'Marigold', 'hex_code': '#C79443'},
    {'name': 'Merlot', 'hex_code': '#32151E'},
    {'name': 'Mid Purple', 'hex_code': '#7768A0'},
    {'name': 'Midnight', 'hex_code': '#14192F'},
    {'name': 'Midnight Blue', 'hex_code': '#161B36'},
    {'name': 'Mint', 'hex_code': '#9FC2CA'},
    {'name': 'Navy', 'hex_code': '#272636'},
    {'name': 'Ocean', 'hex_code': '#181B33'},
    {'name': 'Olive', 'hex_code': '#325942'},
    {'name': 'Onyx', 'hex_code': '#0D0B0E'},
    {'name': 'Orange', 'hex_code': '#E5894A'},
    {'name': 'Pale Seafoam', 'hex_code': '#CBD5BC'},
    {'name': 'Peach', 'hex_code': '#EDB3AF'},
    {'name': 'Pearl', 'hex_code': '#F0F1F3'},
    {'name': 'Peri', 'hex_code': '#667A9D'},
    {'name': 'Pink', 'hex_code': '#F2CEDC'},
    {'name': 'Platinum', 'hex_code': '#EFEEEA'},
    {'name': 'Plum', 'hex_code': '#442E3B'},
    {'name': 'Purple', 'hex_code': '#7C2552'},
    {'name': 'Quartz', 'hex_code': '#A57880'},
    {'name': 'Raspberry', 'hex_code': '#C27683'},
    {'name': 'Red', 'hex_code': '#6C2E2F'},
    {'name': 'Rose', 'hex_code': '#9C676C'},
    {'name': 'Ruby', 'hex_code': '#AB2D42'},
    {'name': 'Seafoam', 'hex_code': '#C6D3B9'},
    {'name': 'Silver', 'hex_code': '#ECEBE9'},
    {'name': 'Silver Sage', 'hex_code': '#9BA29B'},
    {'name': 'Sky Blue', 'hex_code': '#BACFE2'},
    {'name': 'Spearmint', 'hex_code': '#DBDFD5'},
    {'name': 'Steel Blue', 'hex_code': '#7994B7'},
    {'name': 'Tan', 'hex_code': '#C4A98F'},
    {'name': 'Taupe', 'hex_code': '#D5C3AD'},
    {'name': 'Teal', 'hex_code': '#216B90'},
    {'name': 'Tobacco', 'hex_code': '#844B36'},
    {'name': 'Violet', 'hex_code': '#7D5084'},
    {'name': 'White', 'hex_code': '#F1F1EF'},
    {'name': 'Wine', 'hex_code': '#6B2132'},
    {'name': 'Wisteria', 'hex_code': '#B17497'}
]

for c in colors:
    webhexcolor = c['hex_code']
    im = Image.new("RGB", (100,100), webhexcolor)
    image_name = f"{c['name']}_{c['hex_code']}.png"
    im.save(image_name)
    # Make circular
    im = Image.open(image_name)
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)
    im.save(image_name)