import sys
import ezdxf

def mirror_dxf(input_file, output_file, mirror_x=False, mirror_y=False):
    doc = ezdxf.readfile(input_file)
    msp = doc.modelspace()
    
    for entity in msp:
        if entity.dxftype() == "LINE":
            # Modify the start and end points for mirroring
            x1, y1 = entity.dxf.start.x, entity.dxf.start.y
            x2, y2 = entity.dxf.end.x, entity.dxf.end.y
            
            if mirror_x:
                x1, x2 = -x1, -x2
            if mirror_y:
                y1, y2 = -y1, -y2
            
            entity.dxf.start = (x1, y1)
            entity.dxf.end = (x2, y2)
        
        elif entity.dxftype() in ["CIRCLE", "ARC"]:
            x, y = entity.dxf.center.x, entity.dxf.center.y
            if mirror_x:
                x = -x
            if mirror_y:
                y = -y
            entity.dxf.center = (x, y)
        
        elif entity.dxftype() == "LWPOLYLINE":
            new_points = []
            for x, y, *rest in entity.get_points():
                if mirror_x:
                    x = -x
                if mirror_y:
                    y = -y
                new_points.append((x, y, *rest))
            entity.set_points(new_points)
    
    doc.saveas(output_file)
    print(f"Mirrored DXF saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python mirror_dxf.py input.dxf output.dxf mirror_x mirror_y")
        print("Example: python mirror_dxf.py input.dxf output.dxf 1 0 (mirrors X-axis)")
        sys.exit(1)

    input_dxf = sys.argv[1]
    output_dxf = sys.argv[2]
    mirror_x = bool(int(sys.argv[3]))
    mirror_y = bool(int(sys.argv[4]))

    mirror_dxf(input_dxf, output_dxf, mirror_x, mirror_y)
