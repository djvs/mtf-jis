def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

def getfp(b, fname):
  for footprint in b.Footprints().iterator():
    print(footprint.GetReference())
    if footprint.GetReference() == fname:
      return footprint
    print("fuck")
    return None


fp=getfp(b,"H1");fp.SetX( 239.04); fp.SetY(-96.96)

fp=getfp(b,"H2");fp.SetX( 95.60); fp.SetY(-159.88)

fp=getfp(b,"H3");fp.SetX( 143.35); fp.SetY(-159.90)
fp=getfp(b,"H4");fp.SetX( 191.23); fp.SetY(-139.38)
fp=getfp(b,"H5");fp.SetX( 162.99); fp.SetY(-96.99)
fp=getfp(b,"H6");fp.SetX( 177.52); fp.SetY(-55.32)
fp=getfp(b,"H7");fp.SetX( 172.06); fp.SetY(-34.02)
fp=getfp(b,"H8");fp.SetX( 139.05); fp.SetY(-55.25)
fp=getfp(b,"H9");fp.SetX( 111.01); fp.SetY(-75.99)
fp=getfp(b,"H10");fp.SetX( 91.03); fp.SetY(-75.98)
fp=getfp(b,"H11");fp.SetX( 86.44); fp.SetY(-97.25)
fp=getfp(b,"H12");fp.SetX( 63.04); fp.SetY(-54.86)
fp=getfp(b,"H13");fp.SetX( 44.06); fp.SetY(-33.89)
fp=getfp(b,"H14");fp.SetX( 244.01); fp.SetY(-76.00)
fp=getfp(b,"H15");fp.SetX( 253.60); fp.SetY(-55.04)
fp=getfp(b,"H16");fp.SetX( 286.07); fp.SetY(-139.35)
fp=getfp(b,"H17");fp.SetX( 286.83); fp.SetY(-159.94)
fp=getfp(b,"H18");fp.SetX( 400.50); fp.SetY(-75.74)
fp=getfp(b,"H19");fp.SetX( 353.03); fp.SetY(-33.99)

fp=getfp(b,"H20");fp.SetX( 400.02); fp.SetY(-33.94)

fp=getfp(b,"H21");fp.SetX( 19.53); fp.SetY(-159.89)
fp=getfp(b,"H22");fp.SetX( 38.20); fp.SetY(-139.66)
fp=getfp(b,"H23");fp.SetX( 38.20); fp.SetY(-118.49)
fp=getfp(b,"H24");fp.SetX( 21.98); fp.SetY(-97.12)
fp=getfp(b,"H25");fp.SetX( 21.98); fp.SetY(-76.03)
fp=getfp(b,"H26");fp.SetX( 19.82); fp.SetY(-12.94)
fp=getfp(b,"H27");fp.SetX( 63.32); fp.SetY(-12.97)
fp=getfp(b,"H28");fp.SetX( 114.55); fp.SetY(-34.00)
fp=getfp(b,"H29");fp.SetX( 139.31); fp.SetY(-12.97)
fp=getfp(b,"H30");fp.SetX( 168.02); fp.SetY(-76.04)
fp=getfp(b,"H31");fp.SetX( 153.12); fp.SetY(-118.49)
fp=getfp(b,"H32");fp.SetX( 134.04); fp.SetY(-139.37)
fp=getfp(b,"H33");fp.SetX( 95.81); fp.SetY(-118.50)
fp=getfp(b,"H34");fp.SetX( 76.10); fp.SetY(-139.39)
fp=getfp(b,"H35");fp.SetX( 210.51); fp.SetY(-118.49)
fp=getfp(b,"H36");fp.SetX( 248.52); fp.SetY(-139.37)
fp=getfp(b,"H37");fp.SetX( 229.31); fp.SetY(-159.90)
fp=getfp(b,"H38");fp.SetX( 287.06); fp.SetY(-118.46)
fp=getfp(b,"H39");fp.SetX( 315.03); fp.SetY(-97.09)
fp=getfp(b,"H40");fp.SetX( 315.05); fp.SetY(-55.02)
fp=getfp(b,"H41");fp.SetX( 314.99); fp.SetY(-34.05)
fp=getfp(b,"H42");fp.SetX( 314.99); fp.SetY(-12.91)
fp=getfp(b,"H43");fp.SetX( 282.51); fp.SetY(-34.00)
fp=getfp(b,"H44");fp.SetX( 256.02); fp.SetY(-13.00)
fp=getfp(b,"H45");fp.SetX( 210.62); fp.SetY(-12.96)
fp=getfp(b,"H46");fp.SetX( 215.53); fp.SetY(-34.00)
fp=getfp(b,"H47");fp.SetX( 353.03); fp.SetY(-76.01)
fp=getfp(b,"H48");fp.SetX( 372.03); fp.SetY(-76.01)
fp=getfp(b,"H49");fp.SetX( 381.01); fp.SetY(-96.94)
fp=getfp(b,"H50");fp.SetX( 353.05); fp.SetY(-118.48)
fp=getfp(b,"H51");fp.SetX( 372.04); fp.SetY(-159.90)
fp=getfp(b,"H52");fp.SetX( 419.18); fp.SetY(-119.09)
fp=getfp(b,"H53");fp.SetX( 457.00); fp.SetY(-118.92)
fp=getfp(b,"H54");fp.SetX( 381.00); fp.SetY(-55.00)
fp=getfp(b,"H55");fp.SetX( 372.52); fp.SetY(-12.97)

fp=getfp(b,"H56");fp.SetX( 315.05); fp.SetY(-76.05)
fp=getfp(b,"H57");fp.SetX( 353.05); fp.SetY(-138.88)
fp=getfp(b,"H58");fp.SetX( 457.70); fp.SetY(-76.20)
fp=getfp(b,"H59");fp.SetX( 457.70); fp.SetY(-54.84)
fp=getfp(b,"H60");fp.SetX( 457.70); fp.SetY(-33.90)
fp=getfp(b,"H61");fp.SetX( 457.70); fp.SetY(-13.19)
