public class Fridge {
    //assigning variable types
    double size;
    boolean freezer;
    String color;

    //constructor type of three arguments
    //assigning this. to say that it belongs to an object
    public Fridge(double size, boolean freezer, String color) {
        this.size = size;
        this.freezer = freezer;
        this.color = color;
    }
    //returning a description of the fridge such as color, size,and if it provides a freezer
    public String toString() {
        if (freezer) {
            return size + " cubic ft ("+ color +") fridge with freezer";
        } else {
            return size + " cubic ft  ("+ color +") fridge";
        }
    }
}




