public class ElectronicStore {
    //assigning variable
    String name;
    Desktop[] desktops = new Desktop[3];
    Laptop[] laptops = new Laptop[3];
    Fridge[] fridges = new Fridge[3];

    //one argument constructor
    //assigning this. to say that it belongs to an object
    public ElectronicStore(String name) {
        //initializing the name
        this.name = name;

        //preforming arrays for 3 desktops, 3 laptops, 3 fridges and storing all the information in an array
        desktops[0] = new Desktop(3.5, 8, 500, false);
        desktops[1] = new Desktop(3.0, 16, 250, true);
        desktops[2] = new Desktop(4.3, 32, 500, true);

        laptops[0] = new Laptop(3.1, 32, 500, true, 15);
        laptops[1] = new Laptop(2.5, 8, 250, false, 13);
        laptops[2] = new Laptop(3.0, 16, 250, true, 15);

        fridges[0] = new Fridge(16.5, true, "Black ");
        fridges[1] = new Fridge(12.0, true, "White ");
        fridges[2] = new Fridge(23.0, true, " Stainless Steel ");
    }

    //looping through each array and print that object out for the method printStock()
    public void printStock() {
        //printing store
        System.out.println("___________/STORE/_____________");
        //loop through each array and printing the object out
        for (int i = 0; i < desktops.length; i++) {
            System.out.println(desktops[i]);

        }


        for (int i = 0; i < laptops.length; i++) {
            System.out.println(laptops[i]);

        }
        for (int i = 0; i < fridges.length; i++) {
            System.out.println(fridges[i]);
        }
    }

    public boolean searchStock(String searchStock) {
        //case sensitivity
        searchStock = searchStock.toLowerCase();
        //looping through desktops, laptops, and fridges
        for (int i = 0; i < desktops.length; i++) {
            if (desktops[i].toString().toLowerCase().contains(searchStock)) {
                return true;
            }
        }
        for (int i = 0; i < laptops.length; i++) {
            if (laptops[i].toString().toLowerCase().contains(searchStock)) {
                return true;
            }
        }
        for (int i = 0; i < fridges.length; i++) {
            if (fridges[i].toString().toLowerCase().contains(searchStock)) {

            }
        }
        //if the search was not found for an item it will return false
        return false;
    }
}





