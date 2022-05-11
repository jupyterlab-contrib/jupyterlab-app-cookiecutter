import { App } from '../../app/app';

describe('app/app', () => {
  describe('App', () => {
    it('should create an App instance', async () => {
      const app = new App();
      await app.start();
      expect(app).toBeInstanceOf(App);
    });
  });
});
