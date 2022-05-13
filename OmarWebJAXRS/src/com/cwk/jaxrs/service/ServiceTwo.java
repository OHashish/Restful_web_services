package com.cwk.jaxrs.service;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.io.*;

@Path("/two")
public class ServiceTwo {

    @GET
    @Path("/director/{director}")
    @Produces(MediaType.TEXT_HTML)
    public String sayHtmlHello(@PathParam("director") String director) throws IOException {
        //open movies csv file
        BufferedReader br = new BufferedReader(new FileReader("./src/com/cwk/jaxrs/service/movies.csv"));
        String row;
        String Movielist="";
        //loop and parse all lines in file and compare director name in csv file to input
        //if a movie is found ,it is added to the string that is going to be returned
        while ((row = br.readLine()) != null) {
            String[] data = row.split(",");


                if (data[1].equals(director)) {
                    Movielist = Movielist + data[0] +",," ;
                }

        }
        br.close();
        return Movielist;

    }

}
