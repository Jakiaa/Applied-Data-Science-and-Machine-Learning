#A list of coordinate pairs that heps to find center
coords=[(0,0),(2,2),(4,3),(2,-3)]

def centroid(points):
    if not points:
        return None
    
    xs=[p[0] for p in points]
    ys=[p[0] for p in points]
    return (sum(xs)/len(xs), sum(ys)/len(ys))

if __name__=='__main__':
    print("Coordinates: ", coords)
    print("Centroid :", centroid(coords))