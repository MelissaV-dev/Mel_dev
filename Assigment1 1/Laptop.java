public class Laptop {
//assigning variable types
    double CPUSpeed;
    int AmountOfRam;
    int AmountOfStorage;
    Boolean isSSD;
    int ScreenSize;

    // class with 5 argument constructors
    //assigning this. to say that it belongs to an object
    public Laptop(double cpuSpeed, int amountOfRam, int amountOfStorage, boolean isSSD, int screenSize) {
        this.CPUSpeed = cpuSpeed;
        this.AmountOfRam = amountOfRam;
        this.AmountOfStorage = amountOfStorage;
        this.isSSD = isSSD;
        this.ScreenSize = screenSize;
    }
    //providing a description of the laptop
    public String toString() {
        String storageType;
        //check if the storage is SSD or HDD
        if (isSSD) {
            storageType = "SSD Drive";
        } else {
            storageType = "HDD Drive";
        }
        //providing the full description for the laptop such as (screensize, cpu, ram)
        return ScreenSize + " Laptop PC with " + CPUSpeed + " ghz CPU, " + AmountOfRam + " GB RAM, " + AmountOfStorage + " GB " + storageType + ".";

    }
}

