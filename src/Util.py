# pylint: disable=W,R,C



def interpolate_color(c1:tuple[int, int, int], c2:tuple[int, int, int], dx: float) -> tuple[int, int, int]:
    dr = (c2[0] - c1[0]) * dx
    dg = (c2[1] - c1[1]) * dx
    db = (c2[2] - c1[2]) * dx

    return (
        int(c1[0]+dr),
        int(c1[1]+dg),
        int(c1[2]+db)
    )
