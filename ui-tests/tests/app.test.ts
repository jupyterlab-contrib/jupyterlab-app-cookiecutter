import { expect, test } from "@playwright/test";


test.describe("Visual Regression", () => {
  test.beforeEach(async ({ page }) => {
    page.setViewportSize({ width: 1920, height: 1080 });
  });
  test.afterEach(async ({ page, browserName }) => {
    await page.close({ runBeforeUnload: true });
  });

  test("Render app", async ({ page }) => {
    await page.goto('/example');
    await page.waitForSelector('.jp-ExampleWidget');

    expect(await page.screenshot()).toMatchSnapshot({
      name: "render.png",
    });
  });
});
