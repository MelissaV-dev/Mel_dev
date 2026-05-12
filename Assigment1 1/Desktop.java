public class Desktop {
//assigning variable types
    double CPUSpeed;
    int AmountOfRam;
    int AmountOfStorage;
    Boolean isSSD;


    // class with 4 argument constructors
    //assigning this. to say that it belongs to an object
    public Desktop(double cpuSpeed, int amountOfRam, int amountOfStorage, boolean isSSD) {
        this.CPUSpeed = cpuSpeed;
        this.AmountOfRam = amountOfRam;
        this.AmountOfStorage = amountOfStorage;
        this.isSSD = isSSD;


    }

    // toString method where if the ssd is false hdd is for the computer
    public String toString() {
        String AmountoOfStorage;
        //providing an if statement for whether or not the amount of storage corresponds to an SSD or HDD Drive
        if (isSSD) {
            AmountoOfStorage = "SSD Drive";
        } else {
            AmountoOfStorage = "HDD Drive";
        }
        //printing all the desktop's information (ram, cpu, storage)
        return "Desktop's Specs: " + CPUSpeed + " ghz CPU, "
                + AmountOfRam + " GB Ram, "
                + AmountOfStorage + " GB "
                + AmountoOfStorage;
    }
}
