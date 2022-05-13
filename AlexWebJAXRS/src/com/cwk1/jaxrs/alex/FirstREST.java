package com.cwk1.jaxrs.alex;

import java.io.*;
import java.util.Scanner;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.lang.annotation.Target;


@Path("/service1")
public class FirstREST {

    @GET
    @Path("/quote/{quote}")
    @Produces({MediaType.TEXT_PLAIN})
    public String checkQuote(@PathParam("quote") String quote) throws IOException {
        String line = "";
        String result="";
        // Open csv file
        BufferedReader reader = new BufferedReader(new FileReader("./src/com/cwk1/jaxrs/alex/quotes.csv"));
        //Looping through all rows and parse them then compare movie quotes to input
        while((line = reader.readLine()) != null) {

            //use comma as delimter as data is stored in a comma-separated file
            String[] row = line.split(",");
            if(quote.equals(row[0])) {
                result=row[1]+",,"+row[2];
                return result;
            }

        }
        //Return None if no quote was found
        return "None";

    }

}
