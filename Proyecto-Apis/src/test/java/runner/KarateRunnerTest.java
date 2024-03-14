package runner;

import com.intuit.karate.junit5.Karate;

public class KarateRunnerTest {
    //tipos de runner en nuestra ejecucion
    @Karate.Test
    Karate testSample() {
        return Karate.run("classpath:features/create-user.feature",
                "classpath:features/delete-user.feature",
                "classpath:features/search-user.feature",
                "classpath:features/update-user.feature",
                "classpath:features/search-user-update.feature");
    }

}
