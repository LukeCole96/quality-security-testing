package simulationDowntime

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scenarios.TestScenario
import scala.sys.process._
import scala.language.postfixOps

class PeakLoadWithSingleServiceDown extends Simulation {
  val host = "http://localhost:80"

  val httpProtocol = http.baseUrl(host)

  val scenarios = List(
    TestScenario.loginScenario,
    TestScenario.searchScenario
  )

  Process("./src/gatling/scala/scripts/failure_simulation_service_recovery.sh").run()

  setUp(scenarios)
    .protocols(httpProtocol)
    .assertions(
      global.responseTime.percentile(95).lt(1000),
      forAll.successfulRequests.percent.gte(99)
    )
}