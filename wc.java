/* some kind of something 
 */

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class wc{

   public static int getRed(int color){
      return (color >> 16) & 0xff;
   }

   public static int getGreen(int color){
      return (color >> 8) & 0xff;
   }

   public static int getBlue(int color){
      return color & 0xff;
   }

   public static int get_rgb(int color){
      return getRed(color) + getGreen(color) + getBlue(color);
   }

   public static float findIntensity(BufferedImage img, int widthStart, 
                                    int widthEnd, int height){
  
      int phos = 0;

      for(int i = widthStart; i < widthEnd; i++){
         for(int j = 0; j < height; j++){

            int color = img.getRGB(i, j);
            int rgb = get_rgb(color);

            if((rgb) != 0){
               phos++;
            }

         }
      }

      return (float)(phos);
   }

   public static void reportIntensity(float[] arr0, float[] arr1){

      if(arr0.length != arr1.length){
         return;
      }

      float result;
      float[] intensities = new float[arr0.length];

      for(int i = 0; i < arr0.length; i++){
         result = arr1[i]/arr0[i];
         intensities[i] = result;
         System.out.println("The intensity at well " + (i + 1) + " is " + result);
      }
    
   }

   public static void main(String [] args){  

      
      File test = new File("./dots.jpeg");
      File base = new File("./green97.jpeg");
      BufferedImage img = null;
      BufferedImage img0 = null;

      try{
         img = ImageIO.read(test);
         img0 = ImageIO.read(base);
      }
      catch(IOException e){
         System.err.println("No Image available. Please include.");
      }

      int height = img.getHeight();
      int width = img.getWidth();


      int numWells = 3;

      //will hold actual 
      float[] wellArr = new float[numWells];

      //will hold completely saturated(control - ish)
      float[] wellArr0 = new float[numWells];
      
      for(int i = 0; i < numWells; i++){
         int well_startX = i*(width/numWells);
         int well_endX = (i+1)*(width/numWells);

         //finds num of non black pixels per well(for now)
         float intensity = findIntensity(img, well_startX, well_endX, height);
         float intensity0 = findIntensity(img0, well_startX, well_endX, height);

         //store vals in array so can use later
         wellArr[i] = intensity;
         wellArr0[i] = intensity0;
         System.out.println("This is green dots: " + wellArr[i]);
         System.out.println("This is all green: " + wellArr0[i]);
         //System.out.println(intensity0);
      }

      reportIntensity(wellArr0, wellArr);
   }

}
/*
 * going to have 3 regions
 * per region calculate intensity: 
 * all black should be 100%
 * gray should be 50%
 * white should be 0%
 */
