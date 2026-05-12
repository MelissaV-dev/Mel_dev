import java.util.Scanner;

public class TesterProgram {
    public static void main(String[] args) {
        /*//testing for desktop class
        Desktop d1 = new Desktop(3.5, 8, 500, false);
        Desktop d2 = new Desktop(3.0, 16, 250, true);

        Desktop d3 = new Desktop(4.3, 32, 500, true);

        //will be outputted with the toString method I created
        System.out.println(d1);
        System.out.println(d2);
        System.out.println(d3);

        //testing the laptop class
        Laptop l1 = new Laptop(3.1, 32, 500,true,15);
        Laptop l2 = new Laptop(2.5, 8, 250,false,13);
        Laptop l3 = new Laptop(3.0, 16, 250, true, 15);

        //will be outputted with the toString method I created
        System.out.println(l1);
        System.out.println(l2);
        System.out.println(l3);

        //testing out fridge class
        Fridge f1 = new Fridge(16.5,true, "Black");
        Fridge f2 = new Fridge(10.5,false, "White");
        Fridge f3 = new Fridge(23.0,true , " Stainless Steel");

        //will be outputted using the toString method in fridge class
        System.out.println(f1);
        System.out.println(f2);
        System.out.println(f3); */

        //Electronic store test
        ElectronicStore store =new ElectronicStore("Store");
        store.printStock();
        //asking the user to enter an item to search
        Scanner input = new Scanner(System.in);
        //this printing line asks the user to search for an item and to quit if they do not want to search
        System.out.println("Enter An Item To Search, or type quit to exit: ");
        String userInput = input.nextLine();

        while(true) {
            //check if the user would like to quit if so then it will do it
            if(userInput.equalsIgnoreCase("Quit")){
                System.out.println("Goodbye! Not exiting the program.");
                //this is essentially exiting the loop
                break;
            }
            System.out.println("You Searched: " + userInput);
            //The use of searchstock is to see if the item exists
            boolean found = store.searchStock(userInput);

            //using if statement to see if the item is found or not found in the store
            if(found) {
                System.out.println("The item is in the store");
            }else{
                System.out.println("The item does not exist");
            }
            input.close();//this essentially closes the scanner


        }



    }
}

