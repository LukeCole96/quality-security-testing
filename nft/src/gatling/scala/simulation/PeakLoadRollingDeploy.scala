package simulation

import io.gatling.core.Predef._
import io.gatling.core.structure.PopulationBuilder
import io.gatling.http.Predef._
import scenarios.TestScenario

import scala.language.postfixOps
import scala.sys.process.Process

class PeakLoadRollingDeploy extends Simulation {
  val httpProtocol = http
    .baseUrl("http://localhost:80")
    .inferHtmlResources()
    .acceptHeader("application/json")

  val scenarios: List[PopulationBuilder] = List(
    TestScenario.loginScenario,
    TestScenario.searchScenario
  )

  Process("./src/gatling/scala/scripts/rolling_deploy.sh").run()


  setUp(scenarios)
    .protocols(httpProtocol)
    .assertions(
      global.responseTime.percentile(95).lt(1000),
      forAll.successfulRequests.percent.gte(99)
    )
}
