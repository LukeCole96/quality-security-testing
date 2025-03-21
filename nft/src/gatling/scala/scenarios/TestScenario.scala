package scenarios

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

object TestScenario {

  val loginScenario = scenario("User login")
    .exec(
      http("POST /rest/user/login")
        .post("/rest/user/login")
        .header("Content-Type", "application/json")
        .body(StringBody(
          """{
          "email": "admin@juice-sh.op",
          "password": "admin123"
        }"""
        )).asJson
        .check(status.is(200))
    )
    .inject(constantUsersPerSec(100) during (5 minutes))

  val searchScenario = scenario("Search for a product")
    .exec(
      http("GET /rest/products/search?q=apple")
        .get("/rest/products/search?q=apple")
        .check(status.is(200))
    )
    .inject(rampUsersPerSec(1).to(200).during(1.minutes))
}